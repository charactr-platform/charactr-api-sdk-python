import json
import requests
from typing import Callable

from .config import API_URL, ApiVersion
from .data_objects import Audio, Credentials
from .conversion_module import ConversionModule
from .errors import get_api_error
from .tts_stream_simplex import TTSStreamSimplex
from .tts_stream_duplex import TTSStreamDuplex


class TTS(ConversionModule):
    def __init__(self, credentials: Credentials) -> None:
        super().__init__(credentials, "tts")

    def convert(self, voice_id: int, text: str) -> Audio:
        """Convert text to speech with the voice of your choice."""
        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-API-Key": self.credentials["api_key"],
            "Content-Type": "application/json",
        }
        data = {"voiceId": voice_id, "text": text}

        response = requests.post(
            API_URL + "/" + ApiVersion.V1.value + "/" + self.module_name + "/convert",
            headers=headers,
            data=json.dumps(data),
        )

        if response.status_code != 200:
            raise get_api_error(response)

        return Audio(
            data=response.content,
            type=response.headers["Content-Type"],
            duration_ms=response.headers["Audio-Duration-Ms"],
            size_bytes=response.headers["Audio-Size-Bytes"],
        )

    def start_simplex_stream(
        self,
        voice_id: int,
        text: str,
        blocking: bool = True,
        on_data: Callable[[bytes], None] = None,
        on_close: Callable[[int, str], None] = None,
    ) -> TTSStreamSimplex:
        """Simplex streaming allows to send the text to the
        server once and receive the audio response as a stream."""
        return TTSStreamSimplex(
            self.credentials,
            voice_id,
            text,
            blocking=blocking,
            on_data=on_data,
            on_close=on_close,
        )

    def start_duplex_stream(
        self,
        voice_id: int,
        on_data: Callable[[bytes], None] = None,
        on_close: Callable[[int, str], None] = None,
    ) -> TTSStreamDuplex:
        """Duplex streaming allows to send the text to the server multiple times
        and asynchronously receive the audio response as a stream."""
        return TTSStreamDuplex(
            self.credentials, voice_id, on_data=on_data, on_close=on_close
        )
