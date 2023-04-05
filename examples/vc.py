from credentials import CREDENTIALS
from charactr_api import CharactrAPISDK


if __name__ == "__main__":
    sdk = CharactrAPISDK(CREDENTIALS)

    vc_voices = sdk.vc.get_voices()

    with open("./examples/input.wav", mode="rb") as audio_input:
        result = sdk.vc.convert(vc_voices[0]["id"], audio_input)

    with open("result_vc.wav", "wb") as out_f:
        out_f.write(result["data"])

    print("result_vc.wav has been saved.")
    print("Type: ", result["type"])
    print("Size: ", result["size_bytes"], "bytes")
    print("Duration: ", result["duration_ms"], "ms")
