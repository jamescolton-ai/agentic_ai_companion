import os
import json
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import FakeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from tqdm import tqdm

DOCS_DIR = Path("docs")
VECTOR_DIR = Path("vectorstore/index")


def build_index():
    VECTOR_DIR.mkdir(parents=True, exist_ok=True)

    # Load PDFs
    loaders = [PyPDFLoader(str(f)) for f in DOCS_DIR.glob("*.pdf")]
    docs = []
    for loader in loaders:
        docs.extend(loader.load())

    if not docs:
        print("No PDFs found in /docs – add at least one and re-run.")
        return

    # Split
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    # FakeEmbeddings is tiny & local; swap for real model later
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=FakeEmbeddings(size=768),
        persist_directory=str(VECTOR_DIR)
    )
    vectordb.persist()
    print(f"Indexed {len(chunks)} chunks into {VECTOR_DIR}")


if __name__ == "__main__":
    build_index()
