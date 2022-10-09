import random
import turtle
s=["Stone","Paper","Scissors"]
again = True
while(again):
    player=input("Enter Your Choice ('Stone','Paper','Scissors'): ")
    computer=random.choice(s)
    print("Computer : ",computer)
    print("Player : ",player)
    if computer==player:
        print("It's a tie!!! ")
    if computer=="Stone" and player=="Paper":
        print("You Won!!!")
    if computer=="Stone" and player=="Scissors":
        print("Better Luck Next Time!!!")
    if computer=="Paper" and player=="Stone":
        print("Better Luck Next Time!!!")
    if computer=="Paper" and player=="Scissors":
        print("You Won!!!")
    if computer=="Scissors" and player=="Paper":
        print("Better Luck Next Time!!!")
    if computer=="Scissors" and player=="Stone":
        print("You Won!!!")    

    a=input("Do you want to play again (y/n): ")
    if a=="y":
        again=True
    else:
        again=False
