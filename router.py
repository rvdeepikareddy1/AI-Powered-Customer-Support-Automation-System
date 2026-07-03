from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def intent_classifier(state):
    query = state["query"]

    prompt = f"""
You are an expert AI Customer Support Intent Classifier.

Your job is to classify customer queries into ONLY ONE of these departments.

Departments:

1. Sales
- Pricing
- Subscription plans
- Product features
- Product information
- Demo requests

2. Technical
- Application crashes
- Errors
- Installation issues
- Login problems
- Configuration issues

3. Billing
- Refund requests
- Invoice requests
- Payment issues
- Charges
- Transactions

4. Account
- Password reset
- Profile update
- Account activation
- Account deactivation

Customer Query:
{query}

Rules:
- Return ONLY ONE WORD.
- Possible outputs are:
  Sales
  Technical
  Billing
  Account
- Do not explain.
- Do not write any extra text.
"""

    response = llm.invoke(prompt)

    state["intent"] = response.content.strip()

    return state