"""LangChain agent that calls summarize_text.v1 via HTTP."""
import requests
from langchain.agents import initialize_agent, AgentType
from langchain_core.tools import tool
from langchain.llms.fake import FakeListLLM

MCP_URL = "http://localhost:8000"

@tool
def summarize_text(text: str) -> str:
    """Summarize using MCP."""
    resp = requests.post(f"{MCP_URL}/tools/summarize_text.v1", json={"text": text})
    return resp.json().get("summary", "")

llm = FakeListLLM(responses=[
    "Action: summarize_text\nAction Input: This is a long text about agentic AI systems.\nFinal Answer: done"
])

agent = initialize_agent(
    tools=[summarize_text],
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

if __name__ == "__main__":
    print(agent.run("Summarize: Agentic AI combines reasoning and tools."))
