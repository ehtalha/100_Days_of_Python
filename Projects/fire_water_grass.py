# Fire - Water - Grass Game

import random  # used to generate computer choice

# Step 1: Define choices
# f = Fire, w = Water, g = Grass
user_input = input("Enter your choice (f = Fire, w = Water, g = Grass): ")

# Step 2: Dictionary to map input to values
game_dict = {
    "f": 1,   # Fire
    "w": -1,  # Water
    "g": 0    # Grass
}

# Step 3: Reverse dictionary for displaying names
reverse_dict = {
    1: "Fire 🔥",
    -1: "Water 💧",
    0: "Grass 🌿"
}

# Step 4: Generate computer choice randomly
computer = random.choice([1, -1, 0])

# Step 5: Convert user input to value
you = game_dict[user_input]

# Step 6: Show choices
print(f"\nYou chose {reverse_dict[you]}")
print(f"Computer chose {reverse_dict[computer]}")

# Step 7: Game logic
if computer == you:
    print("It's a draw!")

else:
    # Fire vs Grass
    if computer == 1 and you == 0:
        print("You lose! Fire burns Grass.")
    elif computer == 0 and you == 1:
        print("You win! Fire burns Grass.")

    # Grass vs Water
    elif computer == 0 and you == -1:
        print("You lose! Grass absorbs Water.")
    elif computer == -1 and you == 0:
        print("You win! Grass absorbs Water.")

    # Water vs Fire
    elif computer == -1 and you == 1:
        print("You lose! Water extinguishes Fire.")
    elif computer == 1 and you == -1:
        print("You win! Water extinguishes Fire.")

    else:
        print("Something went wrong!")