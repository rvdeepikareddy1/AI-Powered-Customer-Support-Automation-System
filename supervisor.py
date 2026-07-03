from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def review_response(response):

    prompt = f"""
You are a Senior Customer Support Supervisor.

Your task is to review and improve the customer support response.

Improve:
- Grammar
- Professionalism
- Clarity
- Politeness

IMPORTANT:
- Return ONLY the final improved response.
- Do NOT explain your changes.
- Do NOT write "Here is the improved version".
- Do NOT write "I made the following changes".
- Do NOT include bullet points.
- Do NOT add any notes.
- Keep the meaning exactly the same.

Customer Support Response:

{response}
"""

    result = llm.invoke(prompt)

    return result.content.strip()


def supervisor_approval(query):

    print("\n==============================")
    print("SUPERVISOR APPROVAL REQUIRED")
    print("==============================")

    print(f"\nCustomer Request:\n{query}")

    choice = input("\nApprove this request? (yes/no): ").strip().lower()

    return choice == "yes"