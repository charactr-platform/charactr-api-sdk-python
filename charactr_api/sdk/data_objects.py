from typing import TypedDict, List


class Credentials(TypedDict):
    client_key: str
    api_key: str


class VoiceLabel(TypedDict):
    category: str
    label: str


class Voice(TypedDict):
    id: int
    name: str
    description: str
    labels: List[VoiceLabel]
    preview_url: str


def map_voice(api_voice) -> Voice:
    """Map API Voice response to internal Voice dict"""
    return Voice(
        id=api_voice["id"],
        name=api_voice["name"] if "name" in api_voice else "",
        description=api_voice["description"] if "description" in api_voice else "",
        labels=api_voice["labels"] if "labels" in api_voice else [],
        preview_url=api_voice["previewUrl"] if "previewUrl" in api_voice else "",
    )


class Audio(TypedDict):
    data: bytes
    type: str
    duration_ms: int
    size_bytes: int


class TTSMsgType:
    AUTH = "authApiKey"
    CONVERT = "convert"
    CLOSE = "close"


class TTSStreamingOptions(TypedDict):
    format: str
    sample_rate: int
    cloned_voice: bool

class TTSOptions(TypedDict):
    cloned_voice: bool

class VCOptions(TypedDict):
    cloned_voice: bool
