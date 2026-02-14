from joke_teller.crew import CreateJokeCrew

if __name__ == '__main__':
    while True:
        channel = input("Enter an youtube channel handle (format: @exampleChannel): ")
        if channel.startswith('@'):
            break
        print("Error: Channel handle must start with '@'. Please try again.")
    
    crew = CreateJokeCrew().crew()
    inputs = { "channel": channel }
    result = crew.kickoff(inputs=inputs)
