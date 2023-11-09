#QUESTION
'''Class Project:
Implement a Python program that simulates the game of "Rock, Paper, Scissors."
Description: The project should allow two players to input their choices, display the result, and determine the winner based on the rules of the game.
 The program should be interactive and provide user-friendly prompts for input.
PS: Write out your algorithm before coding. Also, do well to comment your code.
'''


# ALGORITHM
# Prompt Player 1 to enter their choice (Rock, Paper, or Scissors)
# Prompt Player 2 to enter their choice (Rock, Paper, or Scissors)
# Use if conditions to check if the choices entered by both players are valid (Rock, Paper, or Scissors)
# If either player's choice is not valid, display "Invalid choice" and terminate the game
# If player1_choice is the same as player2_choice, declare the game a tie.
# Otherwise:
# If player1_choice is "Rock" and player2_choice is "Scissors," Player 1 wins.
# If player1_choice is "Paper" and player2_choice is "Rock," Player 1 wins.
# If player1_choice is "Scissors" and player2_choice is "Paper," Player 1 wins.
# In all other cases, Player 2 wins.





#SOLUTION
# 1. Get the user's choice
player_one = input("Enter your choice (Rock/Paper/Scissors): ").replace(' ',"").capitalize()
player_two = input("Enter your choice (Rock/Paper/Scissors): ").replace(' ',"").capitalize()

# Check for invalid choices
valid_choices = ["Rock", "Paper", "Scissors"]
if player_one not in valid_choices or player_two not in valid_choices:
    print("Invalid choice")
else:

 # 2. Determine the winner
    if player_one == player_two:
        result = "It's a tie!"
    elif (player_one == "Rock" and player_two == "Scissors") or \
        (player_one == "Paper" and player_two == "Rock") or \
        (player_one == "Scissors" and player_two == "Paper"):
        result = "Player one wins!"
    else:
        result = "Player two wins!"

# 3. Display the result
    print(result)



#ORIGINAL SOLLUTION  
# 1. Get the user's choice
player_one = input("Enter your choice (Rock/Paper/Scissors): ").replace(' ',"").capitalize()
player_two = input("Enter your choice (Rock/Paper/Scissors): ").replace(' ',"").capitalize()

# Check for invalid choices
if (
    player_one != "Rock" and player_one != "Paper" and player_one != "Scissors" or
    player_two != "Rock" and player_two != "Paper" and player_two != "Scissors"
):
    print("Invalid choice")
else:

 # 2. Determine the winner
    if player_one == player_two:
        result = "It's a tie!"
    elif (player_one == "Rock" and player_two == "Scissors") or \
        (player_one == "Paper" and player_two == "Rock") or \
        (player_one == "Scissors" and player_two == "Paper"):
        result = "Player one wins!"
    else:
        result = "Player two wins!"

# 3. Display the result
    print(result)