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
To install the package, run in `charactr-api-sdk-python` directory:
```commandline
python setup.py sdist
pip install charactr_api
```
To install the package in editable mode, run in `charactr-api-sdk-python` directory:
```commandline
pip install -e .
```

## Usage
For the detailed SDK usage, please refer to the [SDK Reference](https://docs.api.charactr.com/reference/python) or the `./examples` directory.

## How to run examples
To run examples, install the package in editable mode (see: `Installation`), set your keys in `examples/credentials.py` and type in `charactr-api-sdk-python` directory:
```commandline
python examples/tts.py
```
or
```commandline
python examples/vc.py
```
