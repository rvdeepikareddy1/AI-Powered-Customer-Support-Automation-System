from functools import lru_cache
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


BASE_DIR = Path(__file__).resolve().parent
DOCUMENTS_DIR = BASE_DIR / "documents"


@lru_cache(maxsize=1)
def create_vectorstore():

    files = [
        DOCUMENTS_DIR / "company_policy.txt",
        DOCUMENTS_DIR / "pricing_guide.txt",
        DOCUMENTS_DIR / "technical_manual.txt",
        DOCUMENTS_DIR / "faq.txt"
    ]

    documents = []

    for file in files:

        if not file.exists():
            raise FileNotFoundError(
                f"Document not found: {file}"
            )

        loader = TextLoader(
            str(file),
            encoding="utf-8"
        )

        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore


def retrieve_context(query):

    db = create_vectorstore()

    docs = db.similarity_search(
        query,
        k=2
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context