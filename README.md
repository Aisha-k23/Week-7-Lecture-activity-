# Week 7- Random game

🎮 Game Rules 
The computer secretly chooses a number between 17 and 29 inclusive.

The player rolls a die (1–6).

After each roll, the player decides:

Take another roll, or

Stop

The goal is to get as close as possible to the target number (above or below).

To have a valid turn, the player must finish within 5 of the target.

So if the target is 23, valid totals are:
18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28
(23 ± 5)




⚠️HOW TO ACTUALLY CODE THE GAME INSTRUCRTIONS⚠️
1. Start the program
Add a docstring explaining what the game does.
Import the random module because we need randomness.

2. Computer chooses the target number
Use random.randint(17, 29)
Store it in a variable called target.
Tell the player the range (but not the number).

Why:  
This sets the goal of the game.

3. Set up the player’s total
Create a variable total = 0.
Why:  
We need to keep track of all dice rolls added together.

4. Begin a loop for rolling the die
Use while True: to allow repeated rolls.
Roll the die using random.randint(1, 6).
Add the roll to the total.

Show the player:
the roll
the new total

Why:  
The player must see their progress before deciding whether to continue.

5. Ask the player if they want another roll
Use input("Do you want another roll? (y/n): ").
If they type anything other than "y", break the loop.

Why:  
The player controls when their turn ends.

6. End of turn: show results
Print the target number.
Print the player’s final total.

Why:  
The player needs to see how close they got.

7. Check if the turn is valid
Calculate the distance using abs(total - target).
If the distance is 5 or less, the turn is valid.
Otherwise, it is invalid.

Why:  
This matches the rule:
“To have a valid turn, the player must end no more than 5 from the target.”
