from tools.summarize_text import run

def test_summarize_tool():
    out = run({"text": "Hello world"})
    assert "summary" in out
    assert out["summary"].startswith("Hello")
