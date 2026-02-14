from shared.tracing import traceable
from personal_assistant.crew import PersonalAssistantCrew

@traceable
def main():
    print("Welcome to your Personal Assistant!")
    print("You can ask for jokes, research on topics, or weather forecasts.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nWhat can I help you with today? ")

        # Check if the input is empty or just whitespace
        if not user_input.strip():
            print("Please enter a valid input.")
            continue

        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break

        crew = PersonalAssistantCrew().crew()
        inputs = {"user_request": user_input}
        result = crew.kickoff(inputs=inputs)

        print("\nResult:")
        print(result)


if __name__ == '__main__':
    main()