from listen_command import take_command
from llm_model import gemini_invoke
from speech_to_text import text_to_speech
import streamlit as st

def main():
    st.title("Jarvis Voice Assistant")
    st.write("Ask me anything and I will respond!")

    
    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            user_command = take_command()
            response = gemini_invoke(user_command)
            text_to_speech(response, filename='response.mp3')
            audio_file = open('response.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.text_area("You said:", user_command, height=100)
            st.text_area("Jarvis:", response, height=100)
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button("Download Response", data=audio_bytes, file_name="response.mp3", mime="audio/mp3")
if __name__ == "__main__":
    main()
