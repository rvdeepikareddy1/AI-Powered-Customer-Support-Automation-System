from approval import requires_approval


queries = [
    "I need a refund.",
    "Cancel my subscription.",
    "What are your subscription plans?",
    "I forgot my password.",
    "My application crashes.",
    "I want to speak to management."
]


for query in queries:

    result = requires_approval(query)

    print(f"Query: {query}")
    print(f"Approval Required: {result}")
    print("-" * 40)