import random

game = True

while game:
    choices = ["rock", "paper", "scissor"]

    computer = random.choice(choices)
    user = input("Enter your choice(rock, paper, scissor and \n 'exit' for Exit the game) : ").lower()

    if(computer == user):
        print("User : " + user)
        print("Computer : " + computer)
        print("-----Tie-------")
    elif(user == 'exit'):
        break
    elif(computer == "rock" and user == "scissor"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------Computer Wins -----")
    elif(user == "rock" and computer == "scissor"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------User Wins -----")
    elif(user == "rock" and computer == "paper"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------Computer Wins -----")
    elif(computer == "rock" and user == "scissor"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------User Wins -----")
    elif(user == "paper" and computer == "scissor"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------Computer Wins -----")
    elif(computer == "paper" and user == "scissor"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------User Wins -----")
    else:
        print("\nEnter proper choice \n") 