# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [v2.1.0] - 2023-12-20

- Added Voice Clone support

## [2.0.0] - 2023-08-02

- Changed API URL to [gemelo.ai](https://gemelo.ai)

## [v1.2.0] - 2023-07-26

- Changed User-Agent header to custom value to differentiate SDKs in the backend
- Exposed custom audio format and sample rate settings for TTS Streaming

## [1.1.4] - 2023-05-26

- Added User-Agent header to the WebSocket handshake request

## [1.1.2] - 2023-05-25

- Added Python version requirement to setup.py

## [1.1.1] - 2023-05-19

- Fix releasing-related issue

## [1.1.0] - 2023-05-17

- Added TTS Simplex Streaming
- Added TTS Duplex Streaming

## [1.0.1] - 2023-03-28

We implemented basic SDK features.

### Added

- TTS module
  - making TTS requests
  - fetching TTS voices
- VC module
  - making VC requests
  - fetching VC voices
