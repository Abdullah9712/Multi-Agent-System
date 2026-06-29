import trafilatura


def fetch_webpage(url):

    try:

        downloaded = trafilatura.fetch_url(url)

        if downloaded:

            text = trafilatura.extract(downloaded)

            if text:
                return text[:10000]

        return ""

    except Exception as e:

        print(f"Error fetching {url}: {e}")
        return ""