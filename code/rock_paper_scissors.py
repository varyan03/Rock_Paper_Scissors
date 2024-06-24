#importing random module 
import random

#stored the three possible options in a list
options=["rock","paper","scissors"]

#variables to keep a count of wins of player and comp
comp_wins=0
user_wins=0

while True:

    #generating a interger for the index of the options ,so that a random option can be assigned 
    rand_num=random.randint(0,2)
    comp_choice=options[rand_num]

    #asking user for its choice
    user_choice=input("What do you choose?(rock/paper/scissors/q(if you want to quit))")
    user_choice=user_choice.lower()

    #checking if the user has entered any invalid input
    if user_choice not in options and user_choice!='q':
        print("Enter a valid option")

    #if not satisfied comp wins
        
    else:
        print("Comp Win")
        comp_wins+=1