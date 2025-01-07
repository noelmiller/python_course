import random
import readline
import sys

# Define global variables
moves: dict[str, str] = {"rock": "\U0001FAA8", "paper": "\U0001F4C4", "scissors": "\U00002702"}
valid_moves: list[str] = list(moves.keys())
user_score: int = 0
computer_score: int = 0

# Define text completion function
def completer(text: str, state: int) -> str | None:
    options: list[str] = valid_moves
    matches: list[str] = [opt for opt in options if opt.startswith(text.lower())]
    if state < len(matches):
        return matches[state]
    else:
        return None

# Set up the completer
readline.parse_and_bind('tab: complete')
readline.set_completer(completer)

# Define function to compare scores
def compare_score(user_score: int, computer_score: int) -> None:
    print("----")
    print(f"User score: {user_score}")
    print(f"Computer score: {computer_score}")
    print("----")
    if user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")

# Print welcome message
print("Welcome to Rock, Paper, Scissors!")
print("Enter 'exit' or 'CTRL+C' to quit the game.")


try:
    while True:
        # Get user and computer moves
        user_move: str = input("Enter your move (rock, paper, scissors): ").lower()
        computer_move: str = random.choice(valid_moves)

        # Check if user wants to exit
        if user_move == "exit":
            compare_score(user_score, computer_score)
            sys.exit()

        # Check if user move is valid
        if user_move not in valid_moves:
            print("Invalid move. Please try again.")
            continue

        # print moves
        print("----")
        print(f"User: {moves[user_move]}")
        print(f"Computer: {moves[computer_move]}")
        print("----")

        # Compare moves
        if user_move == computer_move:
            print("It's a draw!")
        elif user_move == "rock" and computer_move == "scissors":
            print("You win!")
            user_score += 1
        elif user_move == "paper" and computer_move == "rock":
            print("You win!")
            user_score += 1
        elif user_move == "scissors" and computer_move == "paper":
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
# Handle exit
except KeyboardInterrupt:
    print("\n")
    compare_score(user_score, computer_score)
    sys.exit(0)
