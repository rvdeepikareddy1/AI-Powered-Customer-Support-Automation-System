from router import classify_intent

queries = [
    "What are your pricing plans?",
    "My application crashes when I upload a file.",
    "I forgot my password.",
    "I need a refund."
]

for q in queries:
    print(f"\nQuery: {q}")
    print("Intent:", classify_intent(q))