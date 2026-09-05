from dotenv import load_dotenv
from langchain_groq import ChatGroq

from rag import retrieve_context


load_dotenv()


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


def generate_response(role, state):

    context = retrieve_context(
        state["query"]
    )

    prompt = f"""
You are a {role}.

Answer the customer's question using only
the company information provided below.

If the answer is not available in the documents,
politely say that the information is not available.

Company Information:

{context}

Customer Question:

{state["query"]}
"""

    response = llm.invoke(prompt)

    state["retrieved_context"] = context
    state["response"] = response.content.strip()

    return state


def sales_agent(state):
    return generate_response(
        "Sales Support Executive",
        state
    )


def technical_agent(state):
    return generate_response(
        "Technical Support Engineer",
        state
    )


def billing_agent(state):
    return generate_response(
        "Billing Support Executive",
        state
    )


def account_agent(state):
    return generate_response(
        "Account Support Executive",
        state
    )