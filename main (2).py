#Rock Paper Scissors Game
import random

while True:
    possible_choice = ["R", "P", "S"]
    user_choice = input("Choose One \nR for Rock, \nP for Paper \nS for Scissors\n: ")
    
    while user_choice not in possible_choice:
        user_choice = input("Enter Valid Input: ")
        break


    if user_choice == "R":
        user_choice_name = "Rock"
    elif user_choice == "P":
        user_choice_name = "Paper"
    else:
        user_choice_name = "Scissors"

    computer_choice = random.choice(possible_choice)
    if computer_choice == "R":
        computer_choice_name = "Rock"
    elif computer_choice == "P":
        computer_choice_name = "Paper"
    else:
        computer_choice_name = "Scissors"

    print(f"\nPlayer ({user_choice_name}): CPU: ({computer_choice_name}).\n")

    if(user_choice == computer_choice):
        print("Both You and Computer chose the same thing")
        result = "Same"
    
    elif((user_choice == "R" and computer_choice == "P") or 
        (user_choice == "P" and computer_choice == "R")):
        print("Paper Wins =>", end = "")
        result = "Paper"
    
    elif((user_choice == "R" and computer_choice == "S") or
        (user_choice == "S" and computer_choice == "R")):
        print("Rock wins =>", end = "")
        result = "Rock"

    else:
        print("Scissors wins =>", end = "")
        result = "Scissors"
    
    if  result == "Same":
        print("<== Draw ==>")
        continue
    elif result == user_choice_name:
        print("<== You Win ==>")
    else:
        print("<== Computer Wins ==>")
    
    print("Do you want to play again? (Y/N)")
    ans = input()
    
    if ans == "N" or ans == "n":
        break

    print("\nThanks for Playing")
    #     if computer_choice == "Scissors":
    #         print("Rock smashes Scissors! You Win!")
    #     else:
    #         print("Paper beats Rock! You Lose.")
    # elif user_choice == "Paper":
    #     if computer_choice == "Rock":
    #         print("Paper covers Rock! You Win!")
    #     else:
    #         print("Scissors beats Paper! You Lose")
    # elif user_choice == "Scissors":
    #     if computer_choice == "Paper":
    #         print("Scissors cuts Paper: You Win!")
    #     else:
    #         print("Rock beats Scissors! You Lose")
    # else:
    #     print("Wrong, Please Try Again")    
        #play_again = input("Play again? (y/n): ")
        #if play_again.lower() != "y":
        #    break