# charactr-api-sdk-python

Python SDK to interact with the charactr API.

## Terminology
**VC** - *Voice conversion* - converting one voice from audio input to another voice.

**TTS** - *Text to speech* - converting text to voice audio.

## Features
- making TTS requests
- making VC requests
- getting lists of available voices

## Installation
```bash
pip install charactr-api-sdk
```

## Usage
For the detailed SDK usage, please refer to the [SDK Reference](https://docs.api.charactr.com/reference/python) or the `./examples` directory.

### Quickstart

```python
from charactr_api import CharactrAPISDK, Credentials

sdk = CharactrAPISDK(Credentials(client_key="xxx", api_key="yyy"))

tts_voices = sdk.tts.get_voices()
tts_result = sdk.tts.convert(tts_voices[0]["id"], "Hello world")
```

## How to run examples

#### Clone & install the SDK locally
```bash
$ git clone https://github.com/charactr-platform/charactr-api-sdk-python
$ cd charactr-api-sdk-python
$ python setup.py sdist
```

#### Provide credentials
Open `./examples/credentials.py` and provide your credentials. You can find them in your [Client Panel](https://api.charactr.com) account.

#### Use TTS
```bash
$ python examples/tts.py
```

#### Use TTS Simplex Streaming
```bash
$ python examples/tts_stream_simplex.py
```

#### Use TTS Duplex Streaming
```bash
$ python examples/tts_stream_duplex.py
```

#### Use VC
```bash
$ python examples/vc.py
```
