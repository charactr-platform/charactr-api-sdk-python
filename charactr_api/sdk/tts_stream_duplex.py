import json
import websocket
import threading

from .data_objects import Credentials, TTSMsgType
from .errors import ConnectionClosedError
from .config import WS_API_URL
from datetime import datetime
from typing import Callable

# defines how long after inactivity the stream will be considered inactive
STREAM_INACTIVITY_THRESHOLD_MS = 5000


class TTSStreamDuplex:
    def __init__(
        self,
        credentials: Credentials,
        voice_id: int,
        on_data: Callable[[bytes], None] = None,
        on_close: Callable[[int, str], None] = None,
    ) -> None:
        self.credentials = credentials
        self.voice_id = voice_id
        self.stream_last_active_at = datetime.now()
        self.is_closed = False
        self.is_close_requested = False
        self.on_data = on_data
        self.on_close = on_close
        self.__on_close_event = threading.Event()

        self.ws = websocket.WebSocketApp(
            WS_API_URL + "/v1/tts/stream/duplex/ws?voiceId=" + str(self.voice_id),
            on_open=self.__on_open,
            on_message=self.__on_message,
            on_close=self.__on_close,
        )

        self.__connect_event = threading.Event()

        wst = threading.Thread(
            target=self.ws.run_forever, kwargs={"ping_interval": 5, "ping_timeout": 2}
        )
        wst.daemon = True
        wst.start()

        self.__connect_event.wait()

    def convert(self, text: str) -> None:
        """Convert text to speech and receive audio response as stream,
        using the `on_data` callback."""
        if self.is_closed or self.is_close_requested:
            raise ConnectionClosedError

        self.ws.send(json.dumps({"type": TTSMsgType.CONVERT, "text": text}))
        self.stream_last_active_at = datetime.now()

    def wait(self) -> None:
        """Blocks execution until there was 5 seconds of stream inactivity."""
        done = threading.Event()

        def awaiter() -> None:
            if not self.__is_stream_active() or self.is_close_requested:
                done.set()
            else:
                threading.Timer(0.5, awaiter).start()

        awaiter()
        done.wait()

    def terminate(self) -> None:
        """Ends the stream immediately. In most cases we advise to use `close()` instead."""
        if self.is_closed:
            return

        self.is_closed = True
        self.ws.close()

    def close(self) -> None:
        """Requests the server to close the connection gracefully."""
        if self.is_closed or self.is_close_requested:
            return

        self.is_close_requested = True
        self.ws.send(
            json.dumps(
                {
                    "type": TTSMsgType.CLOSE,
                }
            )
        )
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
        self.__connect_event.set()

    def __on_message(self, ws: websocket.WebSocketApp, message: bytes) -> None:
        self.stream_last_active_at = datetime.now()

        if self.on_data is not None:
            self.on_data(message)

    def __on_close(
        self, ws: websocket.WebSocketApp, close_status_code: int, close_msg: str
    ) -> None:
        self.is_closed = True
        self.__on_close_event.set()

        if self.on_close is not None:
            self.on_close(close_status_code, close_msg)

    def __ms_since_stream_last_active(self) -> int:
        delta = datetime.now() - self.stream_last_active_at

        return delta.seconds * 1000

    def __is_stream_active(self) -> bool:
        return (
            self.__ms_since_stream_last_active() < STREAM_INACTIVITY_THRESHOLD_MS
            and not self.is_closed
        )
