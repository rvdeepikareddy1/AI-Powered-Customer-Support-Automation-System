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


# Nodes
builder.add_node(
    "Intent",
    intent_classifier
)

builder.add_node(
    "Sales",
    sales_agent
)

builder.add_node(
    "Technical",
    technical_agent
)

builder.add_node(
    "Billing",
    billing_agent
)

builder.add_node(
    "Account",
    account_agent
)


# Starting point
builder.set_entry_point("Intent")


# Decide which agent should handle the query
def route(state):

    intent = state["intent"]

    routes = {
        "Sales": "Sales",
        "Technical": "Technical",
        "Billing": "Billing",
        "Account": "Account"
    }

    return routes.get(intent, "Account")


builder.add_conditional_edges(
    "Intent",
    route
)


# End after the selected agent responds
builder.add_edge("Sales", END)
builder.add_edge("Technical", END)
builder.add_edge("Billing", END)
builder.add_edge("Account", END)


graph = builder.compile()