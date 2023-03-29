import json
import requests
from typing import Dict, List

from .config import API_URL
from .data_objects import Credentials, Voice, map_voice


class VC:
    def __init__(self, credentials: Credentials) -> None:
        self.credentials = credentials

    def get_voices(self) -> List[Voice]:
        """Get the list of available VC voices."""
        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-Api-Key": self.credentials["api_key"],
        }
        response = requests.get(API_URL + "/v1/vc/voices", headers=headers)

        try:
            voices = json.loads(response.content)
        except Exception as e:
            raise Exception(e)
        return list(map(map_voice, voices))

    def convert(self, voice_id: int, input_audio: bytes) -> Dict:
        """Convert one voice to another with audio file input."""
        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-API-Key": self.credentials["api_key"],
        }

        response = requests.post(
            API_URL + "/v1/vc/convert?voiceId=" + str(voice_id),
            headers=headers,
            files=dict(file=input_audio),
        )

        return {
            "data": response.content,
            "type": response.headers["Content-Type"],
            "duration_ms": response.headers["Audio-Duration-Ms"],
            "size_bytes": response.headers["Audio-Size-Bytes"],
        }
