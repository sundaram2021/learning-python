import random

while True:
    choices = ["rock", "paper", "scissor"]

    computer = random.choice(choices);
    user = input("Enter your choice(rock, paper or scissor) : ").lower()

    if(computer == user):
        print("User : " + user)
        print("Computer : " + computer)
        print("-----Tie-------")
        break
    elif(computer == "rock" and user == "scissor"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------Computer Wins -----")
        break
    elif(user == "rock" and computer == "scissor"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------User Wins -----")
        break
    elif(user == "rock" and computer == "paper"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------Computer Wins -----")
        break
    elif(computer == "rock" and user == "scissor"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------User Wins -----")
        break
    elif(user == "paper" and computer == "scissor"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------Computer Wins -----")
        break
    elif(computer == "paper" and user == "scissor"):
        print("User : " + user)
        print("Computer : " + computer)
        print("------User Wins -----")
        break
    else:
        print("Enter proper choice ")    