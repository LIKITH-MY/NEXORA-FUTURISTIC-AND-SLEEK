# search_youtube() goes here
import json
import requests

from urllib.parse import quote_plus
from bs4 import BeautifulSoup

from utils.logger import log_interaction


def search_youtube(query, max_results=10):

    try:

        search_query = quote_plus(query)

        url = (
            f"https://www.youtube.com/results?"
            f"search_query={search_query}"
        )

        headers = {
            "User-Agent":
            "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        scripts = soup.find_all("script")

        videos = []

        for script in scripts:

            if "ytInitialData" not in str(script):
                continue

            try:

                text = str(script)

                start = text.find(
                    "var ytInitialData = "
                ) + len(
                    "var ytInitialData = "
                )

                end = text.find(
                    ";</script>",
                    start
                )

                data = json.loads(
                    text[start:end]
                )

                contents = data.get(
                    "contents", {}
                )

                # Keep original extraction logic

            except:
                continue

        log_interaction(
            "youtube_search",
            query,
            f"{len(videos)} results"
        )

        return videos

    except Exception as e:

        log_interaction(
            "youtube_error",
            query,
            str(e)
        )

        return []
