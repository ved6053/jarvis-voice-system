import pyttsx3

def get_engine():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    return engine
def speak(text: str, rate: int = 150, volume: float = 1.0) -> None:
    """Convert text to speech and play it."""
    engine = get_engine()
    engine.setProperty("rate", rate)      # words per minute
    engine.setProperty("volume", volume)  # 0.0 to 1.0
    engine.say(text)
    engine.runAndWait()


def save_to_file(text: str, filename: str = "output.mp3") -> None:
    engine = get_engine()
    engine.save_to_file(text, filename)
    engine.runAndWait()
def wish_user() -> None:
    """Greet the user based on the time of day."""
    from datetime import datetime

    hour = datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your jarvis voice assistant. How can I help you today?")

if __name__ == "__main__":
    wish_user()
    speak("Hello! This is text to speech using pyttsx3.")
    save_to_file("This sentence is saved to an audio file.", "output.mp3")