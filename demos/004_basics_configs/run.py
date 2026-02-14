from joke_teller.crew import CreateJokeCrew

if __name__ == '__main__':
    topic = input("Enter a topic for the joke: ")
    crew = CreateJokeCrew().crew()
    inputs = { "topic": topic }
    crew.kickoff(inputs=inputs)
