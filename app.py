from graph import graph
from memory import (
    create_database,
    save_conversation,
    get_last_conversation
)
from approval import requires_approval
from supervisor import supervisor_approval, review_response


# Create SQLite database
create_database()

customer_name = "David"

query = input("Customer Query: ").strip()


# ---------------- MEMORY RECALL ----------------

if "previous" in query.lower() and "issue" in query.lower():

    previous = get_last_conversation(customer_name)

    if previous:

        print("\nPrevious Support Issue:")
        print(previous["query"])

        print("\nPrevious Response:")
        print(previous["response"])

    else:

        print("\nNo previous conversation found.")


# ---------------- NORMAL QUERY ----------------

else:

    # Check whether human approval is required
    if requires_approval(query):

        approved = supervisor_approval(query)

        if not approved:

            print("\nRequest Rejected by Supervisor.")
            exit()

        print("\nSupervisor Approved the Request.")

    state = {
        "customer_name": customer_name,
        "query": query,
        "intent": "",
        "retrieved_context": "",
        "approval_required": requires_approval(query),
        "approved": True,
        "response": "",
        "history": ""
    }

    # Run the LangGraph workflow
    result = graph.invoke(state)

    # AI supervisor reviews the generated response
    reviewed_response = review_response(
        result["response"]
    )

    print("\nIntent:", result["intent"])

    print("\nFinal Response:\n")
    print(reviewed_response)

    # Save conversation in SQLite
    save_conversation(
        customer_name,
        result["query"],
        reviewed_response
    )