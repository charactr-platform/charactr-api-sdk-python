from credentials import CREDENTIALS
from charactr_api.sdk.sdk import CharactrAPISDK


if __name__ == "__main__":
    sdk = CharactrAPISDK(CREDENTIALS)

    tts_voices = sdk.tts.get_voices()
    result = sdk.tts.convert("Hello world", tts_voices[0]["id"])

    with open("result_tts.wav", "wb") as out_f:
        out_f.write(result["data"])

    print("result_tts.wav has been saved.")
    print("Type: ", result["type"])
    print("Size (bytes): ", result["size_bytes"])
    print("Duration (ms): ", result["duration_ms"])
