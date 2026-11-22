import speech_recognition as sr
from logger import logging

def take_command(timeout: int = 5, phrase_time_limit: int = 10) -> str:
    """Listen for a voice command and return it as text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        logging.info("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(
                source, timeout=timeout, phrase_time_limit=phrase_time_limit
            )
        except sr.WaitTimeoutError:
            logging.error("No speech detected.")
            return ""

    try:
        logging.info("Recognizing...")
        text = recognizer.recognize_google(audio)
        logging.info(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        logging.error("Could not understand the audio.")
    except sr.RequestError as e:
        logging.error(f"Speech service error: {e}")
    return ""


if __name__ == "__main__":
    command = take_command()
    print("Command:", command)