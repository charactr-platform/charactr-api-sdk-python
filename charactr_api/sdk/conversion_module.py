import json
import requests
from typing import List
from abc import abstractmethod

from .config import API_URL, ApiVersion
from .data_objects import Credentials, Voice, map_voice
from .errors import get_api_error


class ConversionModule:
    def __init__(self, credentials: Credentials, module_name: str) -> None:
        self.credentials = credentials
        self.module_name = module_name

    @abstractmethod
    def get_voices(self) -> List[Voice]:
        """Get the list of available voices."""
        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-Api-Key": self.credentials["api_key"],
        }
        response = requests.get(
            API_URL + "/" + ApiVersion.V1.value + "/" + self.module_name + "/voices",
            headers=headers,
        )

        if response.status_code != 200:
            raise get_api_error(response)

        try:
            voices = json.loads(response.content)
        except Exception as e:
            raise Exception(e)
        return list(map(map_voice, voices))
