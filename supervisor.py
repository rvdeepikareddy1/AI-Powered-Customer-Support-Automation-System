from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


def review_response(response):

    prompt = f"""
You are a customer support supervisor.

Review the response below and improve:

- Grammar
- Clarity
- Professionalism
- Politeness

Keep the original meaning.

Return only the improved response.

Response:

{response}
"""

    result = llm.invoke(prompt)

    return result.content.strip()


def supervisor_approval(query):

    print("\n==============================")
    print("HUMAN APPROVAL REQUIRED")
    print("==============================")

    print(f"\nCustomer Request:\n{query}")

    choice = input(
        "\nApprove this request? (yes/no): "
    ).strip().lower()

    return choice == "yes"