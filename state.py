from typing import TypedDict


class SupportState(TypedDict):
    customer_name: str
    query: str
    intent: str
    retrieved_context: str
    approval_required: bool
    approved: bool
    response: str
    history: str