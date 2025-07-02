"""Simple summarization tool (truncation demo)."""

def run(payload: dict) -> dict:
    text = payload.get("text", "")
    summary = text[:120] + ("..." if len(text) > 120 else "")
    return {"summary": summary}
