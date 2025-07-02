from langchain.agents import initialize_agent, Tool
from langchain_community.llms import Ollama
from tools.web_search import run as web_search
from tools.summarize_text import run as summarize_text
from tools.rag_query import run as rag_query
from langchain.llms.fake import FakeListLLM

llm = FakeListLLM(responses=[
    # Step 1: Pick tool
    "Action: web_search\nAction Input: LangChain updates",

    # Step 2: Tool returns result
    "Observation: LangChain now supports LangGraph, new structured tools, and async agent interfaces.",

    # Step 3: Pick next tool
    "Action: summarize_text\nAction Input: LangChain now supports LangGraph, new structured tools, and async agent interfaces.",

    # Step 4: Summarization result
    "Observation: LangChain added LangGraph and new async tools.",

    # Step 5: Final answer
    "Final Answer: LangChain recently introduced LangGraph and async tool support."
])


# llm = Ollama(model="llama3")

tools = [
    Tool.from_function(
        func=web_search,
        name="web_search.v1",
        description="Search the web. Input should be a search query string."
    ),
    Tool.from_function(
        func=summarize_text,
        name="summarize_text.v1",
        description="Summarize long text. Input should be a dictionary with 'text' key."
    ),
    Tool.from_function(
        func=rag_query,
        name="rag_query.v1",
        description="Semantic search on uploaded PDFs. Input should have 'query' key."
    ),
]

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True
)
