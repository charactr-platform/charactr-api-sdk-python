import json
import requests
from config import API_URL
from data_objects import Credentials, Voice, Audio, map_voice
from typing import List


class TTS:
    def __init__(self, credentials: Credentials) -> None:
        self.credentials = credentials

    def get_voices(self) -> List[Voice]:
        """Get the list of available TTS voices."""
        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-Api-Key": self.credentials["api_key"],
        }
        response = requests.get(API_URL + "/v1/tts/voices", headers=headers)

        try:
            voices = json.loads(response.content)
        except Exception as e:
            raise Exception(e)
        return list(map(map_voice, voices))

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

        return {
            "data": response.content,
            "type": response.headers["Content-Type"],
            "duration_ms": response.headers["Audio-Duration-Ms"],
            "size_bytes": response.headers["Audio-Size-Bytes"],
        }
