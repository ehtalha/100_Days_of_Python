# Fire - Water - Grass Game (With level)
import random

# Step 1: Dictionaries for mapping
game_dict = {
    "f": 1,  # Fire
    "w": -1,  # Water
    "g": 0  # Grass
}

reverse_dict = {
    1: "Fire 🔥",
    -1: "Water 💧",
    0: "Grass 🌿"
}


# Step 2: Function to decide winner
def check_winner(computer, you):
    if computer == you:
        return "draw"

    # Fire vs Grass
    elif computer == 1 and you == 0:
        return "lose"
    elif computer == 0 and you == 1:
        return "win"

    # Grass vs Water
    elif computer == 0 and you == -1:
        return "lose"
    elif computer == -1 and you == 0:
        return "win"

    # Water vs Fire
    elif computer == -1 and you == 1:
        return "lose"
    elif computer == 1 and you == -1:
        return "win"


# Step 3: Initialize scores
user_score = 0
computer_score = 0

# Step 4: Number of rounds
rounds = int(input("Enter number of rounds: "))

print("\nGame Start!\n")

# Step 5: Game loop
for i in range(1, rounds + 1):
    print(f"--- Round {i} ---")

    # Take user input
    user_input = input("Enter (f = Fire, w = Water, g = Grass): ").lower()

    # Handle invalid input
    if user_input not in game_dict:
        print("Invalid input! Try again.\n")
        continue

    # Convert input
    you = game_dict[user_input]
    computer = random.choice([1, -1, 0])

    # Show choices
    print(f"You chose {reverse_dict[you]}")
    print(f"Computer chose {reverse_dict[computer]}")

    # Check result
    result = check_winner(computer, you)

    # Update score
    if result == "win":
        print("You win this round! 🎉")
        user_score += 1
    elif result == "lose":
        print("You lose this round! 😢")
        computer_score += 1
    else:
        print("It's a draw! 🤝")

    print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

# Step 6: Final result
print("=== Final Result ===")
print(f"Your Score: {user_score}")
print(f"Computer Score: {computer_score}")

if user_score > computer_score:
    print("🏆 You are the overall winner!")
elif user_score < computer_score:
    print("💻 Computer wins overall!")
else:
    print("🤝 It's a tie overall!")