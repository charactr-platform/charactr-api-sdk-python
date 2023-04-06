import requests
from typing import Dict, List
from requests_toolbelt.multipart.encoder import MultipartEncoder

from .config import API_URL
from .data_objects import Voice
from .conversion_module import ConversionModule
from .errors import get_api_error


class VC(ConversionModule):
    def get_voices(self) -> List[Voice]:
        """Get the list of available VC voices."""
        return super().get_voices("vc")

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
            API_URL + "/v1/vc/convert?voiceId=" + str(voice_id),
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
