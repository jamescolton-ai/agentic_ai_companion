import sys
import os
import requests
import json

# Ensure project root is on path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_web_search_tool():
    resp = requests.post(
        "http://localhost:8000/tools/web_search.v1",
        json={"query": "LangChain"}
    )
    data = resp.json()
    assert "results" in data and isinstance(data["results"], list)
    assert len(data["results"]) > 0
