"""Web search tool using DuckDuckGo (title-only)."""
import requests, re, html
from bs4 import BeautifulSoup

def run(payload: dict) -> dict:
    query = payload.get("query", "")
    if not query:
        return {"results": []}
    url = f"https://duckduckgo.com/html/?q={query}"
    html_text = requests.get(url, timeout=10).text
    soup = BeautifulSoup(html_text, "html.parser")
    titles = [html.unescape(a.text.strip()) for a in soup.select(".result__title a")[:3]]
    return {"results": titles}
