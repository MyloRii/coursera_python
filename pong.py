# Mini-project "Pong" for
# 'Introduction to Interactive Programming in Python' course at coursera.org
#  made by Joe Warren, John Greiner, Stephen Wong, Scott Rixner

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
direction = random.choice([LEFT, RIGHT])
paddle1_pos = (HEIGHT - PAD_HEIGHT) / 2
paddle2_pos = (HEIGHT - PAD_HEIGHT) / 2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
pause_state = False
pause_msg = " "
ball_vel_pause = [0, 0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        #ball_vel = [3, -1]
        ball_vel[0] = random.randrange(120/60, 240/60)
        ball_vel[1] = random.randrange(-180/60, -60/60)
    elif direction == LEFT:
        ball_vel[0] = random.randrange (-240/60, -120/60)
        ball_vel[1] = random.randrange (-180/60, -60/60)
           
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, direction, pause_state  # these are numbers
    global score1, score2  # these are ints
    if pause_state == False:
        direction = random.choice([LEFT, RIGHT])
        spawn_ball(direction)
        score1 = 0
        score2 = 0
    
def pause():
    global pause_state, pause_msg, ball_vel_pause, ball_vel, paddle1_vel, paddle2_vel
    
    if pause_state == False and (ball_vel[0]!=0 or ball_vel[1]!=0):
        ball_vel_pause[0] = ball_vel[0]
        ball_vel_pause[1] = ball_vel[1]
        ball_vel = [0, 0]
        paddle1_vel = 0
        paddle2_vel = 0  
        pause_state = True
        pause_msg = "Game Paused"
    elif pause_state == True:
        ball_vel[0] = ball_vel_pause[0]
        ball_vel[1] = ball_vel_pause[1]
        pause_state = False
        pause_msg = " "
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
# draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "rgba(255,255,255, 0.5)")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "rgba(255,255,255, 0.5)")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "rgba(255,255,255, 0.5)")
        
# update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
#   incase I forget how to reverse ball with X coordinate from edge of gutter 

#	if ball_pos[0] - BALL_RADIUS <= 0:
#       ball_vel[0] = -ball_vel[0]
#   elif ball_pos[0] >= WIDTH - BALL_RADIUS:
#       ball_vel[0] = -ball_vel[0] 

    if ball_pos[1] - BALL_RADIUS <= 0:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

# this was my mistake. One need to check IF ball hits paddle ELSE it must be reserved. 
# This part is inserted in collide section of code

#    if ball_pos[0] - BALL_RADIUS - PAD_WIDTH <= 0:
#        spawn_ball(RIGHT)
#        score2 += 1
#    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
#        spawn_ball(LEFT)
#        score1 += 1
         
# draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "rgba(192,192,192, 0.5)", "rgb(222,184,135)")
    
# update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= 0 and (paddle1_pos + PAD_HEIGHT) + paddle1_vel <= HEIGHT:
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel >= 0 and (paddle2_pos + PAD_HEIGHT) + paddle2_vel <= HEIGHT:
        paddle2_pos += paddle2_vel
         
# draw paddles
    canvas.draw_line([PAD_WIDTH/2, paddle1_pos],[PAD_WIDTH/2, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "rgb(222,184,135)")
    canvas.draw_line([WIDTH - PAD_WIDTH/2, paddle2_pos],[WIDTH - PAD_WIDTH/2, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "rgb(222,184,135)")
    
# determine whether paddle and ball collide
    if ball_pos[0] - BALL_RADIUS - PAD_WIDTH <= HALF_PAD_WIDTH and (ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] += 0.4
        ball_vel[1] += 0.4
    elif ball_pos[0] - BALL_RADIUS - PAD_WIDTH <= 0:
        spawn_ball(RIGHT)
        score2 += 1

    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH - HALF_PAD_WIDTH and (ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] -= 0.4
        ball_vel[1] -= 0.4
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        spawn_ball(LEFT)
        score1 += 1
        
# draw scores
    canvas.draw_text(str(score1), (WIDTH/4, HEIGHT/4), 35, 'rgb(222,184,135)')
    canvas.draw_text(str(score2), (WIDTH/4 + WIDTH/2 - 30, HEIGHT/4), 35, 'rgb(222,184,135)') 
    
# draw pause message    
    canvas.draw_text(pause_msg, [WIDTH/2 - 60, HEIGHT/2], 24, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP["space"]:
            pause()
    if pause_state == False:
        if key == simplegui.KEY_MAP["N"]:
            new_game()
        if key == simplegui.KEY_MAP["w"]:
            paddle1_vel = -5
        if key == simplegui.KEY_MAP["s"]:
            paddle1_vel = 5
        if key == simplegui.KEY_MAP["up"]:
            paddle2_vel = -5
        if key == simplegui.KEY_MAP["down"]:
            paddle2_vel = 5
                     
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
          
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
#set canvas background
frame.set_canvas_background("rgb(85,107,47)")
# labels
frame.add_label("Pong: The Game")
frame.add_label("Press New game or 'n' to start")
frame.add_label(" ")
frame.add_label("Player 1: ")
frame.add_label("Press 'W' to move up")
frame.add_label("Press 'S' to move down")
frame.add_label(" ")
frame.add_label("Player 2: ")
frame.add_label("Press 'Arrow up' to move up")
frame.add_label("Press 'Arrow down' to move down")
frame.add_label(" ")
# keys
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
# buttons
frame.add_button("New game(n)", new_game, 100)
frame.add_button("Pause(space)", pause, 100)

# start frame
frame.start()

# Andrii Shumylo 2015 (c)
