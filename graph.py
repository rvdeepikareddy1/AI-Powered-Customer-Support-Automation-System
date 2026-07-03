from langgraph.graph import StateGraph, END

from state import SupportState
from router import intent_classifier
from agents import (
    sales_agent,
    technical_agent,
    billing_agent,
    account_agent
)

builder = StateGraph(SupportState)

builder.add_node("Intent", intent_classifier)

builder.add_node("Sales", sales_agent)

builder.add_node("Technical", technical_agent)

builder.add_node("Billing", billing_agent)

builder.add_node("Account", account_agent)


builder.set_entry_point("Intent")


def route(state):

    intent = state["intent"]

    if intent == "Sales":
        return "Sales"

    elif intent == "Technical":
        return "Technical"

    elif intent == "Billing":
        return "Billing"

    else:
        return "Account"


builder.add_conditional_edges(
    "Intent",
    route
)

builder.add_edge("Sales", END)
builder.add_edge("Technical", END)
builder.add_edge("Billing", END)
builder.add_edge("Account", END)

graph = builder.compile()