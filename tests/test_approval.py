from approval import requires_approval

queries = [
    "I need a refund.",
    "Cancel my subscription.",
    "I forgot my password.",
    "My application crashes.",
    "I want to speak to management."
]

for q in queries:
    print(q)
    print("Approval Required:", requires_approval(q))
    print("-" * 40)