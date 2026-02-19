import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock Paper Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to stop.\n")

    while True:
        user_choice = input("Your choice: ").lower().strip()

        if user_choice == "quit":
            print(f"\n🏁 Game Over!")
            print(f"Your Score: {user_score} | Computer Score: {computer_score}")
            if user_score > computer_score:
                print("🏆 YOU WIN OVERALL! Amazing!")
            elif computer_score > user_score:
                print("💻 Computer wins overall. Rematch?")
            else:
                print("🤝 It's a tie overall!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Try again.\n")
            continue

        computer_choice = get_computer_choice()
        result = get_winner(user_choice, computer_choice)

        print(f"\n🤖 Computer chose: {computer_choice}")

        if result == "tie":
            print("🤝 It's a Tie!")
        elif result == "user":
            print("🏆 You Win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        print(f"Score → You: {user_score} | Computer: {computer_score}\n")

play_game()