import json
import requests
from typing import List
from abc import abstractmethod

from .config import API_URL
from .data_objects import Credentials, Voice, map_voice


class ConversionModule:
    def __init__(self, credentials: Credentials) -> None:
        self.credentials = credentials

    @abstractmethod
    def get_voices(self, module_name: str) -> List[Voice]:
        """Get the list of available voices."""
        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-Api-Key": self.credentials["api_key"],
        }
        response = requests.get(
            API_URL + "/v1/" + module_name + "/voices", headers=headers
        )

        try:
            voices = json.loads(response.content)
        except Exception as e:
            raise Exception(e)
        return list(map(map_voice, voices))
