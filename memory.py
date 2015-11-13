# Mini-project "Memory" for
# 'Introduction to Interactive Programming in Python' course at coursera.org
#  made by Joe Warren, John Greiner, Stephen Wong, Scott Rixner

# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global state, turns, exposed, card_deck
    state = 0
    card_list1 = [0, 1, 2, 3, 4, 5, 6, 7]
    card_list2 = [0, 1, 2, 3, 4, 5, 6, 7]
    card_deck = card_list1 + card_list2
    random.shuffle(card_deck)   
    exposed = [False for card in range(16)]
    flipped_card = []
    card1 = 0
    card2 = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    
# define event handlers
def mouseclick(pos):
    # add game state logic here    
    global state, exposed, card1, card2, deck_cards, turns
    click = pos[0] // 50
    
    if state == 0:
        state = 1
        card1 = click
        exposed[card1] = True
    elif state == 1:
        if exposed[click] == False:
            state = 2
            card2 = click
            exposed[card2] = True
            turns += 1   
    elif state == 2:
        if exposed[click] == False:
            if card_deck[card1] != card_deck[card2]:
                exposed[card1] = False
                exposed[card2] = False
            card1 = click
            exposed[card1] = True
            state = 1 
            label.set_text("Turns = " + str(turns))
                     
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    for card in range(len(card_deck)):
        canvas.draw_line([50 * (card % 15 + 1), 0], [50 * (card % 15 + 1 ), 100], 2, "White")
        
        if exposed[card] == True:
            canvas.draw_text(str(card_deck[card]), [15 + 50 * card, 65], 40, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
frame.set_canvas_background('Green')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Andrii Shumylo 2015 (c)
