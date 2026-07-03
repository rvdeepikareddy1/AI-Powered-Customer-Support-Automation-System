from state import SupportState

state = SupportState(
    customer_name="David",
    query="I need a refund",
    intent="",
    retrieved_context="",
    approval_required=False,
    approved=False,
    response="",
    history=""
)

print(state)