import os
import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import importlib
import json
from tools.rag_query import run as rag_query
from fastapi.responses import JSONResponse
from agents.agent_executor import agent_executor

app = FastAPI(title="MCP Server")
METADATA_DIR = Path("metadata")

# Dynamically load tool modules
sys.path.append(str(Path(__file__).resolve().parents[1]))


def load_tool(name: str):
    module = importlib.import_module(f"tools.{name}")
    return module.run


class TextPayload(BaseModel):
    text: str


class QueryPayload(BaseModel):
    query: str


class QueryPayload(BaseModel):
    query: str


class AgentQuery(BaseModel):
    query: str


@app.post("/tools/summarize_text.v1")
def summarize(payload: TextPayload):
    return load_tool("summarize_text")(payload.dict())


@app.post("/tools/web_search.v1")
def search(payload: QueryPayload):
    return load_tool("web_search")(payload.dict())


@app.post("/tools/list")
def list_tools():
    if not METADATA_DIR.exists():
        raise HTTPException(status_code=404, detail="metadata dir missing")
    return {"tools": [f.stem for f in METADATA_DIR.glob("*.json")]}


@app.post("/tools/rag_query.v1")
def rag_endpoint(payload: QueryPayload):
    result = rag_query(payload.dict())
    return JSONResponse(content=result)  # ✅ this ensures proper JSON response


@app.post("/agent")
def run_agent(payload: AgentQuery):
    return {"response": agent_executor.run(payload.query)}
