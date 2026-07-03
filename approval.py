def requires_approval(query):

    query = query.lower()

    approval_keywords = {
        "refund",
        "cancel",
        "subscription",
        "close",
        "closure",
        "delete",
        "compensation",
        "manager",
        "management",
        "escalation"
    }

    return any(keyword in query for keyword in approval_keywords)