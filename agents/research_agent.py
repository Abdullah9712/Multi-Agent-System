from utils.web_search import search_web, fetch_webpage
from utils.api_client import call_model
from utils.file_handler import save_json

class ResearchAgent:
    def run(self, query):
        print("\nSearching for sources...\n")
        search_results = search_web(query)
        print(f"Found {len(search_results)} search results\n")
        collected_data = []
        for i, result in enumerate(search_results, start=1):
            print(f"[{i}] Fetching: {result['title']}")
            print(f"URL: {result['url']}")
            content = fetch_webpage(result["url"])
            print(f"Extracted {len(content)} characters\n")
            if content.strip():
                collected_data.append({
                    "title": result["title"],
                    "url": result["url"],
                    "content": content
                })
        print(f"\nCollected {len(collected_data)} usable sources\n")
        combined_text = ""
        for item in collected_data:
            combined_text += f"""
SOURCE: {item['title']}
URL: {item['url']}

CONTENT:
{item['content'][:5000]}

"""
        print(f"Combined text length: {len(combined_text)}")
        # Fallback if no content was extracted
        if not combined_text.strip():
            print("\nWARNING: No webpage content extracted.")
            print("Falling back to direct model research.\n")
            prompt = f"""
            Research the topic:
            {query}
            Create:
            # Overview
            # Key Concepts
            # Important Facts
            # Current Trends
            """
        else:

            prompt = f"""
You are a research assistant.

Topic:
{query}
Below are extracted webpages.
Use ONLY the information present in these sources.
{combined_text}
Generate:
# Overview
- 5 bullet points
# Key Concepts
- At least 5 concepts
# Important Facts
- 10 facts
# Current Trends
- 5 trends
# References
- List all source URLs
"""
        print("\nSending data to Gemini...\n")
        research = call_model(prompt)
        data = {
            "query": query,
            "source_count": len(collected_data),
            "sources": collected_data,
            "research": research
        }
        save_json(
            data,
            "data/raw/raw_data.json"
        )
        return data