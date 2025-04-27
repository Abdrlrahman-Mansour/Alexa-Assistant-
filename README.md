# Alexa-Assistant

This project is a simple implementation of a voice-based assistant similar to Amazon's Alexa. It uses Python and a combination of libraries for speech recognition, text-to-speech, and some basic functionalities like playing music, answering questions, and more.

## Features

- **Voice Recognition**: Uses speech recognition to understand commands.
- **Text-to-Speech (TTS)**: Responds back with a synthesized voice.
- **Basic Commands**: Allows for a set of predefined actions like playing music, checking the weather, setting reminders, etc.
- **Customizable**: Easily extend the assistant with more functionalities.

## Prerequisites

Make sure you have the following libraries installed:

- `speechrecognition` – For recognizing speech.
- `pyttsx3` – For converting text to speech.
- `pyaudio` – For microphone access.
- `wikipedia` – For getting information from Wikipedia.
- `wolframalpha` – For answering computational queries.
- `datetime` – For handling date and time.
- `os` – For running OS-level commands like opening apps or files.
  
You can install them using pip:

```bash
pip install SpeechRecognition pyttsx3 pyaudio wikipedia wolframalpha

