import sys
from src.joke_flow.flow import JokeFlow
from src.joke_teller.crew import CreateJokeCrew
from shared.tracing import traceable

def validate_topic(topic):
    """Validate that the topic is not empty."""
    if not topic or topic.strip() == "":
        return False
    return True

def get_topic_from_user():
    """Get a topic from the user and validate it."""
    while True:
        topic = input("Enter a topic for a joke (or 'exit' to quit): ")

        if topic.lower() == 'exit':
            print("Goodbye!")
            sys.exit(0)

        if validate_topic(topic):
            return topic
        else:
            print("Topic cannot be empty. Please try again.")

@traceable
def main():
    """Main function to run the joke flow."""
    print("Welcome to the Joke Generator!")
    print("-------------------------------")

    while True:
        # Get and validate topic from user
        topic = get_topic_from_user()

        try:
            # Create and run the joke flow
            print(f"\nGenerating a joke about '{topic}'...\n")

            # Create a joke flow with the given topic
            flow = JokeFlow(topic=topic)

            # Run the flow and get the result
            result = flow.kickoff()

            # Print the joke
            if result:
                print("\n=== Your Joke ===")
                print(result)
                print("=================\n")
            else:
                print("Sorry, couldn't generate a joke. Please try another topic.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        # Ask if the user wants to continue
        continue_choice = input("\nWould you like another joke? (y/n): ")

        if continue_choice.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
