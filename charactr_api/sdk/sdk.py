from .data_objects import Credentials, TTSStreamingOptions
from .tts import TTS
from .vc import VC
from .clones import VoiceClone


class CharactrAPISDK:
    def __init__(self, credentials: Credentials) -> None:
        self.credentials = credentials
        self.tts = TTS(credentials)
        self.vc = VC(credentials)
        self.voice_clone = VoiceClone(credentials)
