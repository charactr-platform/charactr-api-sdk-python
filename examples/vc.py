from credentials import CREDENTIALS
from charactr_api.sdk.sdk import CharactrAPISDK


if __name__ == "__main__":
    sdk = CharactrAPISDK(CREDENTIALS)

    vc_voices = sdk.tts.get_voices()

    with open("./examples/input.wav", mode="rb") as audio_input:
        result = sdk.vc.convert(audio_input, vc_voices[0]["id"])

    with open("result_vc.wav", "wb") as out_f:
        out_f.write(result["data"])

    print("result_vc.wav has been saved.")
    print("Type: ", result["type"])
    print("Size (bytes): ", result["size_bytes"])
    print("Duration (ms): ", result["duration_ms"])
