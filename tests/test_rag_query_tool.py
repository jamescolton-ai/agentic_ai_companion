import sys
import os
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_rag_query():
    resp = requests.post(
        "http://localhost:8000/tools/rag_query.v1",
        json={"query": "agentic"}
    )
    data = resp.json()
    assert "answer" in data and len(data["answer"]) > 20
