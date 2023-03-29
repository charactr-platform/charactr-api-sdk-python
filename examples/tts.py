import sys

from sdk.sdk import CharactrAPISDK
from credentials import CREDENTIALS

if __name__ == "__main__":
    sdk = CharactrAPISDK(CREDENTIALS)

    tts_voices = sdk.tts.get_voices()
    result = sdk.tts.convert("Hello world", tts_voices[0]["id"])

    f = open("result_tts.wav", "wb")
    f.write(result["data"])
    f.close()

    print("result_tts.wav has been saved.")
    print("Type: ", result["type"])
    print("Size (bytes): ", result["size_bytes"])
    print("Duration (ms): ", result["duration_ms"])
