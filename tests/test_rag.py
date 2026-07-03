from rag import create_vectorstore

db = create_vectorstore()

print("Vector Database Created Successfully")

print()

print("Total Chunks :", db.index.ntotal)