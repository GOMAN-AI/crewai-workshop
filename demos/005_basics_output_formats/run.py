from joke_teller.crew import CreateJokeCrew

if __name__ == '__main__':
    topic = input("Enter a topic for the joke: ")
    crew = CreateJokeCrew().crew()
    inputs = { "topic": topic }
    result = crew.kickoff(inputs=inputs)
    joke_with_explanation = result.pydantic
    print(joke_with_explanation.joke)
