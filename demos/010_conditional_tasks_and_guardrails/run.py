from joke_teller.crew import CreateJokeCrew
from shared.tracing import traceable

@traceable
def main():
    while True:
        channel = input("Enter an youtube channel handle (format: @exampleChannel): ")
        if channel.startswith('@'):
            break
        print("Error: Channel handle must start with '@'. Please try again.")

    crew = CreateJokeCrew().crew()
    inputs = { "channel": channel }
    crew.kickoff(inputs=inputs)

if __name__ == '__main__':
    main()
