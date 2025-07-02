# Agentic AI Companion – Code Repo

This repository accompanies **Agentic AI Systems with LangChain + MCP + RAG + Ollama (Companion v2)** by **James Colton**.

## Quick Start

```bash
git clone <repo-url>
cd agentic-ai-companion
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# run MCP server
uvicorn server.mcp_server:app --reload

# call first tool
curl -X POST http://localhost:8000/tools/summarize_text.v1 \
     -H "Content-Type: application/json" \
     -d '{"text":"Agentic AI blends reasoning and tools."}'

# run agent demo
python agents/simple_agent.py
```

## Folder Map
* `tools/` – Python functions callable as MCP tools  
* `metadata/` – JSON specs describing each tool  
* `server/` – FastAPI MCP server implementation  
* `agents/` – LangChain agent scripts  
* `ingestion/` – RAG ingestion pipelines (chap 5)  
* `tests/` – Pytest smoke tests  
* `docs/` – Sample docs for embedding  
* `vectorstore/` – Saved FAISS indices  

## Chapters
The code is organised to align with each book chapter:

* **Chapter 4** – `summarize_text` tool, MCP server  
* **Chapter 5** – ingestion pipeline (to be added)  
* **Chapter 6** – `web_search` tool + composable agent demo  
* Further chapters add deployment, multi‑agent, etc.
