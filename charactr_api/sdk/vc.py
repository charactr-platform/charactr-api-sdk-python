import requests
from typing import Dict
from requests_toolbelt.multipart.encoder import MultipartEncoder

from .config import API_URL, ApiVersion
from .data_objects import Credentials
from .conversion_module import ConversionModule
from .errors import get_api_error


class VC(ConversionModule):
    def __init__(self, credentials: Credentials) -> None:
        super().__init__(credentials, "vc")

    def convert(self, voice_id: int, input_audio: bytes) -> Dict:
        """Convert one voice to another with audio file input."""
        multipart_data = MultipartEncoder(
            fields={"file": ("file.wav", input_audio, "audio/wav")}
        )

        headers = {
            "X-Client-Key": self.credentials["client_key"],
            "X-API-Key": self.credentials["api_key"],
            "Content-Type": multipart_data.content_type,
        }

        response = requests.post(
            API_URL
            + "/"
            + ApiVersion.V1.value
            + "/"
            + self.module_name
            + "/convert?voiceId="
            + str(voice_id),
            headers=headers,
            data=multipart_data,
        )

        if response.status_code != 200:
            raise get_api_error(response)

        return {
            "data": response.content,
            "type": response.headers["Content-Type"],
            "duration_ms": response.headers["Audio-Duration-Ms"],
            "size_bytes": response.headers["Audio-Size-Bytes"],
        }
