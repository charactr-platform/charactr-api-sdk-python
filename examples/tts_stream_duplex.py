from credentials import CREDENTIALS
from charactr_api import CharactrAPISDK


if __name__ == "__main__":
    sdk = CharactrAPISDK(CREDENTIALS)

    with open("result_tts_stream_duplex.wav", "wb") as out_f:

        def on_data(data: bytes) -> None:
            out_f.write(data)

        def on_close(code: int, message: str) -> None:
            if code != 1000:
                raise Exception("Error [{0}]: {1}".format(code, message))
            else:
                print("result_tts_stream_duplex.wav has been saved.")

        tts_voices = sdk.tts.get_voices()

        stream = sdk.tts.start_duplex_stream(
            tts_voices[0]["id"], on_data=on_data, on_close=on_close
        )
        stream.convert("Hello world from the charactr TTS Duplex Streaming.")
        stream.convert("You can send as much text as you want asynchronously.")
        stream.close()
