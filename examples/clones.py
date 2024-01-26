from credentials import CREDENTIALS
from charactr_api import CharactrAPISDK


if __name__ == "__main__":
    sdk = CharactrAPISDK(CREDENTIALS)

	# create/update/load cloned voices
    voice_id = 0
    with open("./examples/inputclone.opus", mode="rb") as audio_clone_input:
        voice = sdk.voice_clone.create_cloned_voice("test-voice-sdk", audio_clone_input)
        voice_id = voice["id"]
        print("Voice created: ", voice_id, voice["name"])

    voice = sdk.voice_clone.update_cloned_voice(voice_id, "test-voice-sdk-rename")
    print("Voice updated: ", voice_id, voice["name"])

    voices = sdk.voice_clone.get_cloned_voices()
    print("Number of cloned voices: ", len(voices))

    # tts
    tts_voices = sdk.tts.get_voices()
    result = sdk.tts.convert(voice_id, "Hello world", { "cloned_voice": True })

    with open("result_tts.wav", "wb") as out_f:
        out_f.write(result["data"])

    print("result_tts.wav has been saved.")

    # tts streaming
    with open("result_tts_stream_simplex.wav", "wb") as out_f:
        def on_data(data: bytes) -> None:
            out_f.write(data)
        def on_close(code: int, message: str) -> None:
            if code != 1000:
                raise Exception("Error [{0}]: {1}".format(code, message))
            else:
                print("result_tts_stream_simplex.wav has been saved.")

        text = "Hello world from the charactr TTS Simplex Streaming."

        stream = sdk.tts.start_simplex_stream(
            voice_id, text, on_data=on_data, on_close=on_close, options={"cloned_voice": True}
        )

    # vc
    with open("./examples/input.wav", mode="rb") as audio_input:
        result = sdk.vc.convert(voice_id, audio_input, { "cloned_voice": True })

    with open("result_vc.wav", "wb") as out_f:
        out_f.write(result["data"])
        print("result_vc.wav has been saved.")
    
    # delete test voice
    sdk.voice_clone.delete_cloned_voice(voice_id)
    print("Voice deleted")


