from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def create_vectorstore():

    files = [
        "documents/company_policy.txt",
        "documents/pricing_guide.txt",
        "documents/technical_manual.txt",
        "documents/faq.txt"
    ]

    documents = []

    for file in files:
        loader = TextLoader(file)
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

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    return context