from tts import TTS
from vc import VC
from data_objects import Credentials


class CharactrAPISDK:
    def __init__(self, credentials: Credentials) -> None:
        self.credentials = credentials
        self.tts = TTS(credentials)
        self.vc = VC(credentials)
