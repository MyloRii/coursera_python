# Mini-project "Guess the number"
# 'Introduction to Interactive Programming in Python' Course at coursera.org
# by Joe Warren, John Greiner, Stephen Wong, Scott Rixner
# Made by Andrii Shumylo 2015 (c)

# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import simplegui
import random

def new_game():
    # global variables used in code
    global num_range
    num_range = 7
    print "New game. Range is from 0 to 100.\nNumber of remaining guesses is", num_range
    print
    global secret_number
    secret_number = random.randrange(0, 101)

# event handlers for control panel
# button that changes the range to [0,100) and starts a new game 
def range100():
    global num_range
    num_range = 7
    print "You've chosen the range between 0 and 100.\nNumber of remaining guesses is", num_range
    global secret_number
    secret_number = random.randrange(0, 101)
    
# button that changes the range to [0,1000) and starts a new game     
def range1000():
    global num_range
    num_range = 10
    print "You've chosen the range between 0 and 1000.\nNumber of remaining guesses is", num_range
    global secret_number
    secret_number = random.randrange(0, 1001)
    
# main game logic goes here	 
def input_guess(guess):
    print "Guess was", int(guess)
    guess = int(guess)
    if guess == secret_number:
        print "Correct!"
        new_game()
    elif guess > secret_number:
        print "Lower!"
        global num_range
        num_range -= 1
        print "Number of remaining guesses is", num_range
    elif guess < secret_number:
        print "Higher!"
        num_range -= 1
        print "Number of remaining guesses is", num_range
    else: 
        print "Something is wrong"
        
    if num_range == 0:
        print "You are out of guesses"
        print
        new_game()
    else:
        print
         
# frame
frame = simplegui.create_frame("Guess game", 200, 200)

# registered event handlers for control elements and start frame
frame.add_button("Range is [0, 100]", range100, 200)
frame.add_button("Range is [0, 1000]", range1000, 200)
frame.add_input("Enter your guess here", input_guess, 200)
frame.start()

# call new_game 
new_game()
