# Jarvis Voice Assistant

Jarvis is a Python-based personal AI voice assistant for Windows. It listens
through the microphone, converts speech to text, uses Google's Gemini model to
answer natural-language questions, and can speak or play the response.

Jarvis also provides a Streamlit web interface and a console assistant mode.

## Features

- Voice recognition using Google Speech Recognition
- Gemini-powered chat assistance using `google-genai`
- Multilingual Gemini responses that match the user's language
- Text-to-speech using `gTTS`, with `pyttsx3` and Windows SAPI5 available for
  console playback
- Streamlit voice chat interface with text and downloadable MP3 responses
- Time-based greeting
- Current time responses
- Wikipedia answers
- Google and YouTube launcher
- Console and file logging

## Requirements

- Windows
- Python 3.12
- A working microphone
- Internet access for speech recognition, Gemini, Wikipedia, and `gTTS`
- [uv](https://docs.astral.sh/uv/) installed
- A Google Gemini API key

## Installation

Open a terminal in the `jarvis-system` project folder:

```powershell
cd jarvis-system
uv sync
```

This creates a `.venv` environment and installs the project dependencies.

Install the additional packages used by the Streamlit and console interfaces:

```powershell
uv add streamlit gTTS wikipedia pyaudio
```

## Configure Gemini

Create a Gemini API key, then set it in the current PowerShell session:

```powershell
$env:GOOGLE_GEMINI_API_KEY = "your-api-key"
```

To keep the variable available for future terminal sessions:

```powershell
[Environment]::SetEnvironmentVariable(
    "GOOGLE_GEMINI_API_KEY",
    "your-api-key",
    "User"
)
```

Jarvis uses `gemini-3.5-flash-lite` by default. The model can be changed in
`src/jarvis_system/llm_model.py`.

## Run the Streamlit Voice Chat

```powershell
uv run --env-file .env streamlit run src/jarvis_system/main.py
```

Open the local URL displayed by Streamlit. Select **Ask me anything**, speak
your question, and Jarvis will:

1. Convert the microphone input to text.
2. Send the question to Gemini.
3. Display both the recognized question and Gemini response.
4. Generate an MP3 response that can be played or downloaded.

## Run the Console Assistant

```powershell
uv run python src/jarvis_system/jarvis_console.py
```

Jarvis will greet you and listen for commands. Say one of the following:

- `What time is it?`
- `What is your name?`
- `Open Google`
- `Open YouTube`
- Ask any general question for a Gemini response
- `Exit` or `Quit`
- Any Wikipedia topic, such as `Albert Einstein`

For example:

- `What is quantum computing?`
- `Explain photosynthesis in Hindi`
- `Tell me a short story in Spanish`

Gemini is configured to reply briefly in plain text and in the same language as
the user's question. The current speech recognition and text-to-speech helpers
use their default English language settings unless configured otherwise in
`listen_command.py` and `speech_to_text.py`.

## Project Structure

```text
jarvis-system/
|-- src/
|   `-- jarvis_system/
|       |-- __init__.py
|       |-- jarvis_console.py
|       |-- listen_command.py
|       |-- llm_model.py
|       |-- logger.py
|       |-- main.py
|       `-- speech_to_text.py
|-- logs/
|   `-- application.log
|-- pyproject.toml
|-- uv.lock
`-- README.md
```

## Manual Dependency Installation

If dependencies are not managed through `uv`, install them with:

```powershell
pip install SpeechRecognition pyttsx3 pyaudio wikipedia google-genai gTTS streamlit
```

## Output

- Gemini responses are shown in text and can be generated as speech in MP3
  format.
- Console responses can be spoken through the system voice.
- Activity and recognition messages are printed in the terminal.
- Log messages are saved in `logs/application.log`.
- Text-to-speech test audio can be saved as `output.mp3`.
- Streamlit response audio is saved as `response.mp3`.

## Troubleshooting

- **No microphone detected:** Check Windows microphone permissions and ensure a
  microphone is selected as the default input device.
- **No speech recognized:** Speak clearly, reduce background noise, and verify
  internet access.
- **No spoken audio:** Confirm that a Windows voice is installed and that
  system audio is enabled.
- **Gemini authentication error:** Make sure `GOOGLE_GEMINI_API_KEY` is set in
  the same terminal session where Jarvis is started.
- **Missing package:** Run `uv sync` and install the additional packages listed
  in the installation section.