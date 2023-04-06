import json
import requests
from typing import List

from .config import API_URL
from .data_objects import Voice, Audio
from .conversion_module import ConversionModule
from .errors import get_api_error


class TTS(ConversionModule):
    def get_voices(self) -> List[Voice]:
        """Get the list of available TTS voices."""
        return super().get_voices("tts")

    def convert(self, voice_id: int, text: str) -> Audio:
        """Convert text to speech with the voice of your choice."""
        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-API-Key": self.credentials["api_key"],
            "Content-Type": "application/json",
        }
        data = {"voiceId": voice_id, "text": text}

        response = requests.post(
            API_URL + "/v1/tts/convert", headers=headers, data=json.dumps(data)
        )

        if response.status_code != 200:
            raise get_api_error(response)

        return Audio(
            data=response.content,
            type=response.headers["Content-Type"],
            duration_ms=response.headers["Audio-Duration-Ms"],
            size_bytes=response.headers["Audio-Size-Bytes"],
        )
