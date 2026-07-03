from rag import retrieve_context

query = "What are your pricing plans?"

context = retrieve_context(query)

print("Retrieved Context:\n")
print(context)