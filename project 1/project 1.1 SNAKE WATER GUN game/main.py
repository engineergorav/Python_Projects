# SNAKE WATER GUN game

'''
-1 == snake
 1 == water
 0 == gun
'''
import random

computer=random.choice([-1,1,0])

user=(input("enter your choice { s , w , g }: ")).lower()

if(user!="s" and user!= "w" and user!= "g"):
    print("invalid entery! please retry again:   ")
    exit()

elif(user== "s" or user == "g" or user == "w"):
    user_choice = { "s" : -1 , "w" : 1 , "g" : 0 }
    computer_choice = { -1 : "snake" , 1 : "Water" , 0 : "Gun" }
    item=user_choice[user]

    print(f"you chose {computer_choice[item]}\nand computer chose {computer_choice[computer]}")

    if(computer == item):
        print("Match is draw! ")
    else:
        outcome={
                 (-1,0):"You WIN: ",
                 (-1,1):"You LOSE: ",
                 (1,-1):"You Win: ",
                 (1,0):"You LOSE: ",
                 (0,1):"You WIN: ",
                 (0,-1):"You LOSE: "
                }
        print(outcome[computer,item])