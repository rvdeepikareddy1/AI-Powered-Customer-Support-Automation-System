from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


def classify_intent(query):
    prompt = f"""
You are a customer support intent classifier.

Classify the customer query into exactly ONE department.

Departments:

Sales:
- Pricing
- Subscription plans
- Product features
- Product information
- Demo requests

Technical:
- Application crashes
- Errors
- Installation problems
- Login problems
- Configuration problems

Billing:
- Refunds
- Invoices
- Payments
- Charges
- Transactions

Account:
- Password reset
- Profile updates
- Account activation
- Account deactivation

Customer Query:
{query}

Return ONLY ONE of these words:

Sales
Technical
Billing
Account
"""

    response = llm.invoke(prompt)

    intent = response.content.strip()

    # Make sure the output is one of our valid departments
    valid_intents = ["Sales", "Technical", "Billing", "Account"]

    for department in valid_intents:
        if department.lower() in intent.lower():
            return department

    # Default department if the model gives an unexpected answer
    return "Account"


def intent_classifier(state):
    state["intent"] = classify_intent(state["query"])
    return state