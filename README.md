# Jarvis Voice Assistant

Jarvis is a Python-based personal voice assistant for Windows. It listens through
the microphone, converts speech to text, speaks responses, searches Wikipedia,
and opens common websites.

## Features

- Voice recognition using Google Speech Recognition
- Text-to-speech using `pyttsx3` and the Windows SAPI5 engine
- Time-based greeting
- Current time responses
- Wikipedia answers
- Google and YouTube launcher
- Console and file logging

## Requirements

- Windows
- Python 3.12
- A working microphone
- Internet access for speech recognition and Wikipedia
- [uv](https://docs.astral.sh/uv/) installed

## Installation

Open a terminal in the `jarvis-system` project folder:

```powershell
cd jarvis-system
uv sync
```

This creates a `.venv` environment and installs the project dependencies.

## Run Jarvis

```powershell
uv run python src/jarvis_system/main.py
```

Jarvis will greet you and listen for commands. Say one of the following:

- `What time is it?`
- `What is your name?`
- `Open Google`
- `Open YouTube`
- `Exit` or `Quit`
- Any Wikipedia topic, such as `Albert Einstein`

## Project Structure

```text
jarvis-system/
|-- src/
|   `-- jarvis_system/
|       |-- __init__.py
|       |-- listen_command.py
|       |-- logger.py
|       |-- main.py
|       `-- speech_to_text.py
|-- pyproject.toml
|-- uv.lock
`-- README.md
```

## Manual Dependency Installation

If dependencies are not managed through `uv`, install them with:

```powershell
uv add speechrecognition pyttsx3 pyaudio wikipedia
```

## Output

- Spoken responses are generated through the system voice.
- Activity and recognition messages are printed in the terminal.
- Log messages are saved in `logs/application.log`.
- Text-to-speech test audio can be saved as `output.mp3`.

## Troubleshooting

- **No microphone detected:** Check Windows microphone permissions and ensure a
  microphone is selected as the default input device.
- **No speech recognized:** Speak clearly, reduce background noise, and verify
  internet access.
- **No spoken audio:** Confirm that a Windows voice is installed and that
  system audio is enabled.