from langchain_community.embeddings import FakeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path

VECTOR_DIR = Path("vectorstore/index")


def run(payload: dict) -> dict:
    query = payload.get("query", "")
    if not query:
        return {"answer": "", "sources": []}

    vectordb = Chroma(
        embedding_function=FakeEmbeddings(size=768),
        persist_directory=str(VECTOR_DIR)
    )
    docs_and_scores = vectordb.similarity_search_with_score(query, k=3)

    # Simple answer: concatenate top chunks
    answer_parts, sources = [], []
    for doc, score in docs_and_scores:
        answer_parts.append(doc.page_content.strip())
        sources.append(doc.metadata.get("source", ""))
    answer = " ".join(answer_parts)[:400] + "..."

    return {"answer": answer, "sources": sources}
