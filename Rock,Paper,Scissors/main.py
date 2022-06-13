import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
								+"Rock beats Scissors \n"
								+"Paper beats Rock \n"
								+"Scissors beats Paper \n")

R = "rock"
P = "paper"
S = "scissors"

while True:

    user_action = input("Pick an option (R, P, S): ")
    possible_options = ["R", "P", "S"]
    computer_action = random.choice(possible_options)
    user_action == possible_options
    print(f"\nPlayer chose {user_action} : , CPU chose {computer_action}.\n")
    
    while user_action not in possible_options:
        print= input("You chose an invalid command. Pick an option (R, P, S): ")


    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie! Play again")

    elif user_action == "R": 
        if computer_action == "S":
            print("Rock beats Scissors! You win!")
        else:
            print("Paper beats Rock! You lose.")
    elif user_action == "P": 
        if computer_action == "R":
            print("Paper beats Rock! You win!")
        else:
            print("Scissors beats Paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors beats Paper! You win!")
        else:
            print("Rock beats Scissors! You lose.")



    Endgame = input("Play again? (Y/N): ")
    if Endgame=="N":
        break

print("Goodbye")
           
