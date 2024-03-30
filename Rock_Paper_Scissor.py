import random

reset_game = 4
while reset_game == 4:
    # Intro
    print("\n\n*************** Welcome To Rock Paper Scissor Game ***************")
    print("Press 1 for Rock\nPress 2 for Paper\nPress 3 for Scissor")
    input_from_user = int(input("Enter Your Choice : "))
    
    computer_choices = random.choice([1,2,3])
    # User Wins
    if input_from_user == 1:
        if computer_choices == 3:
            print("Congrats! You Win, You Choose Rock and Computer Choose Scissor.")
    elif input_from_user == 2:
        if computer_choices == 1:
            print("Congrats! You Win, You Choose Paper and Computer Choose Rock.")
    elif input_from_user == 3:
        if computer_choices == 2:
            print("Congrats! You Win, You Choose Scissor and Computer Choose Paper.")
    else:
        print("Please Try Again...")

    # Draw Match
    if input_from_user == 1:
        if computer_choices == 1:
            print("It's Tie, Both You and Computer Choose Rock.")
    elif input_from_user == 2:
        if computer_choices == 2:
            print("It's Tie, Both You and Computer Choose Paper.")
    elif input_from_user == 3:
        if computer_choices == 3:
            print("It's Tie, Both You and Computer Choose Scissor.")
    else:
        pass


    # Computer Wins
    if computer_choices == 1:
        if input_from_user == 3:
            print("You Lose, You Choose Scissor and Computer Choose Rock.")
    elif computer_choices == 2:
        if input_from_user == 1:
            print("You Lose, You Choose Rock and Computer Choose Paper.")
    elif computer_choices == 3:
        if input_from_user == 2:
            print("You Lose, You Choose Paper and Computer Choose Scissor.")
    else:
        pass

    reset_game = int(input("Do you want to continue or exit? (4/5) : "))