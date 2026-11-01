'''
Workflow ofproject
1- input (Rock , paper, scissor)
2 - computer (computer will choose random)
3- result

cases
A - Rock
Rock(i) - Rock(computer) =tie
Rock-paper =Paper win
Rock - scissor = Rock win

B - Papaer
Paper -paper = tie
paper - rock = Paper wing
Papaer - scissor = Scissor win

C- Scissor

Scissor- Scissor= tie
Scissor - rock = rock win
Scissor= paper = Scissor win


'''

import random #import random module

item_list=["Rock","Paper","Scissor"] #store value in variable
print("******************************** ROCK, PAPER and SCISSOR GAME ***************************************")
user_choice=input("Enter your move = Rock, Paper, Scissor = ")
computer_choice = random.choice(item_list) # random.choice is function in random which we define import random

print(f"User choice= {user_choice},Computer choice ={computer_choice}")

if user_choice==computer_choice:
    print("Tie")
elif user_choice=="Rock":
    if computer_choice =="Paper":
     print("Paper covers Rocks = Computer win")
    else:
     print("Rock smashes Scissor = you Win :-) ")

elif user_choice=="Paper":
    if computer_choice=="Scissor":
        print(" Scissor cutes paper, Computer Win")
    else:
        print("paper covers rock, You win")
elif user_choice=="Scissor" :
    if computer_choice=="Paper":
        print("Scissor cuts paper , You win")
    else:
        print("Rock smashes scissor, computer win")