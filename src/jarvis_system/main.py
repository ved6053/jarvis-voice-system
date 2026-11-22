from listen_command import take_command
from speech_to_text import speak, wish_user
import webbrowser
import wikipedia
def answer_wikipedia_query(query: str) -> None:
    """Answer a user's query using Wikipedia."""
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Your query is ambiguous. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I could not find any information on that topic.")
    except Exception as e:
        speak(f"An error occurred while fetching information: {e}")
def talk_to_user():
    """Continuously listen for user commands and respond."""
    wish_user()
    while True:
        command = take_command()
        if 'time' in command:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        elif 'name' in command:
            speak("I am Jarvis, your personal voice assistant.")
        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye! Have a great day!")
            break
        elif command != '':
            answer_wikipedia_query(command)
if __name__ == "__main__":
    talk_to_user()
        