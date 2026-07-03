from memory import *

create_database()

save_conversation(
    "David",
    "I have a billing issue.",
    "Billing response"
)

print(get_last_query("David"))