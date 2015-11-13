# Mini-project Rock-paper-scissors-lizard-Spock
# 'Introduction to Interactive Programming in Python' Course at coursera.org
# by Joe Warren, John Greiner, Stephen Wong, Scott Rixner
# Made by Andrii Shumylo 2015 (c)

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    if name == "rock":
        name = 0
        return name
    elif name == "Spock":
        name = 1
        return name
    elif name == "paper":
        name = 2
        return name
    elif name == "lizard":
        name = 3
        return name
    elif name == "scissors":
        name = 4
        return name
    else:
        print "Nope, you did the wrong thing"

def number_to_name(number):
    if number == 0:
        number = "rock"
        return number
    elif number == 1:
        number = "Spock"
        return number
    elif number == 2:
        number = "paper"
        return number
    elif number == 3:
        number = "lizard"
        return number
    elif number == 4:
        number = "scissors"
        return number
    else:
        print "Nope, you did the wrong thing"
       
def rpsls(player_choice):
    
    # print a blank line to separate consecutive games 
    print
    
    # print out the message for the player's choice  
    print "Player chooses " + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
     # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    
    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print "Player and computer tie"
    elif difference == 1 or difference == 2:
        print "Player wins"
    else: 
        print "Computer wins"   
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
