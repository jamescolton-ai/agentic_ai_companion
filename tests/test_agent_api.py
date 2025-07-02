import requests


def test_agent_api():
    resp = requests.post(
        "http://localhost:8000/agent",
        json={"query": "What is LangChain? Use the tools."}
    )
    data = resp.json()
    assert "response" in data
    assert len(data["response"]) > 20
