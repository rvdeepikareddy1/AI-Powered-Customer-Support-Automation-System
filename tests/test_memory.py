from memory import (
    create_database,
    save_conversation,
    get_last_conversation
)


create_database()


save_conversation(
    "TestUser",
    "I have a billing issue.",
    "Please contact our billing team."
)


conversation = get_last_conversation(
    "TestUser"
)


print("Previous Conversation:")

if conversation:

    print(
        "Query:",
        conversation["query"]
    )

    print(
        "Response:",
        conversation["response"]
    )

else:

    print("No conversation found.")