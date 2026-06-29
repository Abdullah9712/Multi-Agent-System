import json


def extract_json(response):

    try:

        response = response.strip()

        if response.startswith("```json"):
            response = response[7:]

        if response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        return json.loads(response)

    except Exception as e:

        print(f"JSON Parse Error: {e}")
        return None