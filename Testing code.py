
from random import randint

def roll_dice():
    return randint(1, 6)

# Test the function
# We use range(10) here to test the dice function 10 times.
# It is NOT part of the real game — it's just to check that roll_dice() works.
for _ in range(10):
    print(roll_dice())

# Set Total to Zero initially for before you roll a die
total = 0

# FOREVER- ie this code written will loop forever because we have written 'while true'
while True:
    # Roll a Die
    roll = roll_dice()
    print(f"You rolled a {roll}")

# Add the roll to the Total
total = total + roll

# Tell the user what the total is
print(f"Your total is now {total}")


