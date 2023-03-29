import sys

from sdk.sdk import CharactrAPISDK
from credentials import CREDENTIALS

if __name__ == "__main__":
    sdk = CharactrAPISDK(CREDENTIALS)

    vc_voices = sdk.tts.get_voices()

    audio_input = open("./examples/input.wav", mode="rb")
    result = sdk.vc.convert(audio_input, vc_voices[0]["id"])
    audio_input.close()

    result_file = open("result_vc.wav", "wb")
    result_file.write(result["data"])
    result_file.close()

    print("result_vc.wav has been saved.")
    print("Type: ", result["type"])
    print("Size (bytes): ", result["size_bytes"])
    print("Duration (ms): ", result["duration_ms"])
