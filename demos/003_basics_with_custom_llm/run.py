from crewai import Agent, Task, Crew
from textwrap import dedent
from shared.llm import LMSTUDIO_DEEPSEEK_LLM

def tell_joke(topic: str) -> str:
    # Create a comedian agent
    comedian = Agent(
        llm=LMSTUDIO_DEEPSEEK_LLM,
        role='Comedian',
        goal='Create hilarious and engaging jokes',
        backstory=dedent("""
            You are a professional stand-up comedian with years of experience in
            crafting jokes. You have a great sense of humor and can create jokes
            about any topic while keeping them appropriate and entertaining.
        """),
        verbose=True
    )

    # Create a task for joke creation
    create_joke = Task(
        description=dedent(f"""
                   Create a funny joke about {topic}. The joke should be
                   original, appropriate, and entertaining. Format it nicely
                   with setup and punchline.
            """),
        expected_output="A funny joke about the given topic",
        agent=comedian
    )

    # Create a crew with our comedian
    crew = Crew(
        agents=[comedian],
        tasks=[create_joke],
        verbose=True
    )

    # Get the result
    result = crew.kickoff()

    return result.raw

if __name__ == '__main__':
    # Get the topic from user input
    topic = input("Enter a topic for the joke: ")
    tell_joke(topic)
