import json
import requests

from .config import API_URL, ApiVersion
from .data_objects import Audio, Credentials
from .conversion_module import ConversionModule
from .errors import get_api_error


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
            API_URL + "/" + ApiVersion.V1 + "/" + self.module_name + "/convert", headers=headers, data=json.dumps(data)
        )

        if response.status_code != 200:
            raise get_api_error(response)

        return Audio(
            data=response.content,
            type=response.headers["Content-Type"],
            duration_ms=response.headers["Audio-Duration-Ms"],
            size_bytes=response.headers["Audio-Size-Bytes"],
        )
