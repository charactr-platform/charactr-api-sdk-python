import json

import websocket
import threading

from .data_objects import Credentials, TTSMsgType
from .config import WS_API_URL
from typing import Callable


class TTSStreamSimplex:
    def __init__(
        self,
        credentials: Credentials,
        voice_id: int,
        text: str,
        blocking: bool = True,
        on_data: Callable[[bytes], None] = None,
        on_close: Callable[[int, str], None] = None,
    ) -> None:
        self.credentials = credentials
        self.voice_id = voice_id
        self.text = text
        self.on_data = on_data
        self.on_close = on_close
        self.__on_close_event = threading.Event()

        self.ws = websocket.WebSocketApp(
            WS_API_URL + "/v1/tts/stream/simplex/ws?voiceId=" + str(self.voice_id),
            on_open=self.__on_open,
            on_message=self.__on_message,
            on_close=self.__on_close,
        )

        wst = threading.Thread(
            target=self.ws.run_forever, kwargs={"ping_interval": 5, "ping_timeout": 2}
        )
        wst.daemon = True
        wst.start()

        if blocking:
            self.__on_close_event.wait()

    def __on_open(self, ws: websocket.WebSocketApp) -> None:
        self.ws.send(
            json.dumps(
                {
                    "type": TTSMsgType.AUTH,
                    "clientKey": self.credentials["client_key"],
                    "apiKey": self.credentials["api_key"],
                }
            )
        )
        self.ws.send(json.dumps({"type": TTSMsgType.CONVERT, "text": self.text}))

    def __on_message(self, ws: websocket.WebSocketApp, message: bytes) -> None:
        if self.on_data is not None:
            self.on_data(message)

    def __on_close(
        self, ws: websocket.WebSocketApp, close_status_code: int, close_msg: str
    ) -> None:
        self.__on_close_event.set()

        if self.on_close is not None:
            self.on_close(close_status_code, close_msg)
