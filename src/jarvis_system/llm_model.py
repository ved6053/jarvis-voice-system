import os

from google import genai
from google.genai import types

MODEL = "gemini-3.5-flash-lite"  # You can change this to any other Gemini model available

# Create the client once and reuse it, not on every call
_client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))


def gemini_invoke(user_input: str) -> str:
    """Generate a response using the Gemini model."""
    response = _client.models.generate_content(
        model=MODEL,
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are Jarvis, a voice assistant. Reply briefly in plain text "
                "with no markdown, in the same language as the user."
            ),
        ),
    )
    return response.text or ""


if __name__ == "__main__":
    query = input("Enter your query for the Gemini model: ")
    print(gemini_invoke(query))