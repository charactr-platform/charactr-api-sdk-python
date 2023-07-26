from urllib.parse import urlencode

from .data_objects import TTSStreamingOptions


def get_tts_streaming_query_params(
    voice_id: int, options: TTSStreamingOptions = None
) -> str:
    params = {"voiceId": str(voice_id)}

    if options is not None:
        if "sample_rate" in options and "format" not in options:
            options["format"] = "wav"

        if "format" in options:
            params["format"] = options["format"]

        if "sample_rate" in options:
            params["sr"] = str(options["sample_rate"])

    return urlencode(params)
