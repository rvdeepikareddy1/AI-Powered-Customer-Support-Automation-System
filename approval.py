def requires_approval(query):

    query = query.lower()

    risky_requests = [
        "refund",
        "cancel my subscription",
        "cancel the subscription",
        "cancel my account",
        "close my account",
        "close the account",
        "delete my account",
        "delete the account",
        "compensation",
        "speak to a manager",
        "speak to management",
        "talk to a manager",
        "talk to management",
        "escalate this",
        "escalate my issue"
    ]

    return any(request in query for request in risky_requests)