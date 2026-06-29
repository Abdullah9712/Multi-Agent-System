from ddgs import DDGS
import requests
from bs4 import BeautifulSoup


def search_web(query, max_results=5):

    results = []

    try:

        with DDGS() as ddgs:

            search_results = ddgs.text(
                query,
                max_results=max_results
            )

            for item in search_results:

                print(f"Found: {item.get('title', 'No Title')}")

                results.append({
                    "title": item.get("title", ""),
                    "url": item.get("href", "")
                })

    except Exception as e:

        print(f"Search Error: {e}")

    return results


def fetch_webpage(url):

    try:

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for script in soup(["script", "style"]):
            script.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text[:10000]

    except Exception as e:

        print(f"Error fetching {url}: {e}")
        return ""