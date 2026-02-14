from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from textwrap import dedent


def tell_joke(topic: str) -> str:
    # Create the prompt with comedian persona (matching CrewAI agent definition)
    prompt = ChatPromptTemplate.from_messages([
        ("system", dedent("""
            You are a Comedian.

            Goal: Create hilarious and engaging jokes

            Backstory: You are a professional stand-up comedian with years of experience in
            crafting jokes. You have a great sense of humor and can create jokes
            about any topic while keeping them appropriate and entertaining.
        """)),
        ("human", dedent("""
            Create a funny joke about {topic}. The joke should be
            original, appropriate, and entertaining. Format it nicely
            with setup and punchline.

            Expected output: A funny joke about the given topic
        """))
    ])

    # Create the LLM
    llm = ChatOpenAI(model="gpt-4o-mini")

    # Create the chain: prompt | llm | output_parser
    chain = prompt | llm | StrOutputParser()

    # Invoke the chain and get the result
    result = chain.invoke({"topic": topic})

    print(result)
    return result


if __name__ == '__main__':
    # Get the topic from user input
    topic = input("Enter a topic for the joke: ")
    tell_joke(topic)
