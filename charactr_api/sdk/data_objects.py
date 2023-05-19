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
        name=api_voice["name"],
        description=api_voice["description"],
        labels=api_voice["labels"],
        preview_url=api_voice["previewUrl"],
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
