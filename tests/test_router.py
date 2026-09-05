from router import classify_intent


queries = [
    "What are your pricing plans?",
    "My application crashes when I upload a file.",
    "I forgot my password.",
    "I need a refund."
]


for query in queries:

    intent = classify_intent(query)

    print(
        f"Query: {query}"
    )

    print(
        f"Intent: {intent}"
    )

    print("-" * 40)