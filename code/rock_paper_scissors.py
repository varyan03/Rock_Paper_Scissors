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