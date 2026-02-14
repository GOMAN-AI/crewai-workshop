import os
from src.heads_or_tails.crew import HeadsOrTailsCrew
from shared.tracing import traceable

os.environ["DOCKER_HOST"] = "tcp://dind:2375"

@traceable
def main():
    while True:
        print("\n=== Heads or Tails Game ===")
        player_guess = input("Enter your guess (Head or Tail): ").strip().capitalize()

        # Validate input
        if player_guess not in ["Head", "Tail"]:
            print("Invalid input! Please enter either 'Head' or 'Tail'.")
            continue

        crew = HeadsOrTailsCrew().crew()
        inputs = {"player_guess": player_guess}
        response = crew.kickoff(inputs=inputs)

        print("\nGame Result:")
        print(response.raw)

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == '__main__':
    main()
