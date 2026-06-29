from datetime import datetime

from utils.file_handler import load_json, save_json
from utils.api_client import call_model
from utils.helpers import extract_json


class CleaningAgent:

    def run(self):

        print("\n=== Cleaning Agent ===\n")

        raw_data = load_json(
            "data/raw/raw_data.json"
        )

        if not raw_data:

            return {
                "error": "raw_data.json not found or empty"
            }

        query = raw_data.get("query", "")
        research = raw_data.get("research", "")
        sources = raw_data.get("sources", [])

        if not research:

            return {
                "error": "No research data available"
            }

        # Prevent extremely large prompts
        research = research[:12000]

        source_count = len(sources)

        references = []

        for source in sources:

            url = source.get("url")

            if url:
                references.append(url)

        print(f"Sources: {source_count}")
        print(f"Research Length: {len(research)} characters")

        prompt = f"""
You are an expert data cleaning and preprocessing agent.

TOPIC:
{query}

RESEARCH:
{research}

TASK:

Convert the research into clean structured JSON.

RULES:

* Remove duplicate information.
* Remove repeated facts.
* Remove markdown symbols.
* Remove unnecessary formatting.
* Remove website noise.
* Keep only useful factual information.
* Write a concise executive summary.
* Organize information clearly.
* Keep content professional and readable.

IMPORTANT:

* Return ONLY valid JSON.
* No markdown.
* No code fences.
* No explanations.
* No comments.
* No extra text.

JSON FORMAT:

{{
"topic": "",
"executive_summary": "",
"overview": [],
"key_concepts": [],
"important_facts": [],
"current_trends": []
}}
"""

        print("\nCleaning data...")
        print(f"Prompt Length: {len(prompt)} characters")

        cleaned_response = call_model(prompt)

        print("\nModel response received")

        cleaned_json = extract_json(
            cleaned_response
        )

        if cleaned_json is None:

            cleaned_json = {
                "topic": query,
                "error": "Model returned invalid JSON",
                "raw_response": cleaned_response
            }

        # Metadata
        cleaned_json["generated_at"] = (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        cleaned_json["source_count"] = (
            source_count
        )

        cleaned_json["references"] = (
            references
        )

        save_json(
            cleaned_json,
            "data/cleaned/clean_data.json"
        )

        print(
            "\nSaved cleaned data to:"
            " data/cleaned/clean_data.json"
        )

        return cleaned_json
