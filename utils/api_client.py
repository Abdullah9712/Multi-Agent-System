from google import genai
from config import GEMINI_API_KEY, MODEL_NAME
import time

client = genai.Client(api_key=GEMINI_API_KEY)


def call_model(prompt: str) -> str:

    MAX_RETRIES = 5

    for attempt in range(MAX_RETRIES):

        try:

            print(
                f"\nSending request to Gemini "
                f"(Attempt {attempt + 1}/{MAX_RETRIES})..."
            )

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            if (
                response
                and hasattr(response, "text")
                and response.text
            ):
                return response.text

            raise Exception("Empty response received")

        except Exception as e:

            print(f"\nError: {e}")

            if attempt < MAX_RETRIES - 1:

                wait_time = 2 ** attempt

                print(
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

            else:

                print(
                    "\nAll retries failed."
                )

    return """
{
    "error": "Gemini unavailable"
}
"""