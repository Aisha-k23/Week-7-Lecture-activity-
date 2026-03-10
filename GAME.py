"""lbu-random-game
This is a simple dice game"""

import random

# Computer chooses target
target = random.randint(17, 29)
print("I am thinking of a number between 17 and 29...")

total = 0

while True:
    roll = random.randint(1, 6)
    print(f"\nYou rolled a {roll}.")
    total += roll
    print(f"Your total is now {total}.")

    # Ask player if they want another roll
    choice = input("Do you want another roll? (y/n): ").strip().lower()

    if choice != "y":
        break

# End of turn
print("\n--- Turn Finished ---")
print(f"Target number: {target}")
print(f"Your final total: {total}")

# Check if valid turn
if abs(total - target) <= 5:
    print("Valid turn! You finished within 5 of the target.")
else:
    print("Invalid turn. You were too far from the target.")
