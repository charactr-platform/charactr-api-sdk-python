import json
import requests
from typing import Dict, List
from requests_toolbelt.multipart.encoder import MultipartEncoder

from .config import API_URL, ApiVersion
from .data_objects import Credentials, map_voice, Voice
from .conversion_module import ConversionModule
from .errors import get_api_error


class VoiceClone():
    def __init__(self, credentials: Credentials) -> None:
        self.credentials = credentials

    def get_cloned_voices(self) -> List[Voice]:
        """Get the list of user cloned voices."""
        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-Api-Key": self.credentials["api_key"],
            "Content-Type": "application/json",
            "User-Agent": "sdk-python",
        }
        response = requests.get(
            API_URL + "/" + ApiVersion.V1.value + "/cloned-voices?limit=500",
            headers=headers,
        )

        if response.status_code != 200:
            raise get_api_error(response)

        try:
            jsonresp = json.loads(response.content)
            voices = jsonresp.get("items", [])
        except Exception as e:
            raise Exception(e)
        return list(map(map_voice, voices))

    def create_cloned_voice(self, name: str, input_audio: bytes) -> Voice:
        """Create a new cloned voice with provided name, that sounds like provided audio"""
        multipart_data = MultipartEncoder(
            fields={
                "name": name,
                "audio": ("file.wav", input_audio, "audio/wav")
            }
        )

        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-API-Key": self.credentials["api_key"],
            "Content-Type": multipart_data.content_type,
            "User-Agent": "sdk-python",
        }

        response = requests.post(
            API_URL
            + "/"
            + ApiVersion.V1.value
            + "/cloned-voices",
            headers=headers,
            data=multipart_data,
        )

        if response.status_code != 200:
            raise get_api_error(response)

        try:
            voice = json.loads(response.content)
        except Exception as e:
            raise Exception(e)
        return voice

    def update_cloned_voice(self, voice_id: int, name: str) -> Voice:
        """Update the name of the cloned voice"""

        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-API-Key": self.credentials["api_key"],
            "Content-Type": "application/json",
            "User-Agent": "sdk-python",
        }

        data = {"name": name}

        response = requests.patch(
            API_URL
            + "/"
            + ApiVersion.V1.value
            + "/cloned-voices/"
            + str(voice_id),
            headers=headers,
            data=json.dumps(data),
        )

        if response.status_code != 200:
            raise get_api_error(response)

        try:
            voice = json.loads(response.content)
        except Exception as e:
            raise Exception(e)
        return voice

    def delete_cloned_voice(self, voice_id: int) -> None:
        """Deletes the cloned voice"""

        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-API-Key": self.credentials["api_key"],
            "User-Agent": "sdk-python",
        }

        response = requests.delete(
            API_URL
            + "/"
            + ApiVersion.V1.value
            + "/cloned-voices/"
            + str(voice_id),
            headers=headers,
        )

        if response.status_code != 204:
            raise get_api_error(response)

