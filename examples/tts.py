from credentials import CREDENTIALS
from charactr_api import CharactrAPISDK


if __name__ == "__main__":
    sdk = CharactrAPISDK(CREDENTIALS)

    tts_voices = sdk.tts.get_voices()
    result = sdk.tts.convert(tts_voices[0]["id"], "Hello world")

    with open("result_tts.wav", "wb") as out_f:
        out_f.write(result["data"])

    print("result_tts.wav has been saved.")
    print("Type: ", result["type"])
    print("Size: ", result["size_bytes"], "bytes")
    print("Duration: ", result["duration_ms"], "ms")
