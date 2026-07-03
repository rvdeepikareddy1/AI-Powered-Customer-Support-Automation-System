from graph import graph
from memory import create_database, save_conversation, get_last_query
from approval import requires_approval
from supervisor import supervisor_approval, review_response

# Create SQLite database
create_database()

customer_name = "David"

query = input("Customer Query : ")

# ---------------- MEMORY RECALL ----------------

if "previous" in query.lower() and "issue" in query.lower():

    previous = get_last_query(customer_name)

    print("\nPrevious Support Issue:")
    print(previous)

else:

    state = {
        "customer_name": customer_name,
        "query": query,
        "intent": "",
        "department": "",
        "retrieved_context": "",
        "approval_required": False,
        "approved": False,
        "response": "",
        "history": ""
    }

    result = graph.invoke(state)

    # AI Supervisor reviews every response
    reviewed_response = review_response(result["response"])

    # Human approval only for risky requests
    if requires_approval(query):

        approved = supervisor_approval(query)

        if not approved:

            print("\nRequest Rejected by Supervisor.")

        else:

            print("\nSupervisor Approved the Request.")

            print("\nIntent :", result["intent"])

            print("\nFinal Response:\n")

            print(reviewed_response)

            save_conversation(
                customer_name,
                result["query"],
                reviewed_response
            )

    else:

        print("\nIntent :", result["intent"])

        print("\nFinal Response:\n")

        print(reviewed_response)

        save_conversation(
            customer_name,
            result["query"],
            reviewed_response
        )