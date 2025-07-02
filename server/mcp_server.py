from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import importlib, json

app = FastAPI(title="MCP Server")
METADATA_DIR = Path("metadata")

# Dynamically load tool modules
import sys, os
sys.path.append(str(Path(__file__).resolve().parents[1]))

def load_tool(name: str):
    module = importlib.import_module(f"tools.{name}")
    return module.run

class TextPayload(BaseModel):
    text: str

class QueryPayload(BaseModel):
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
