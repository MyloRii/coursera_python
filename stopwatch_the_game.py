# Mini-project "Stopwatch: The Game" for
# 'Introduction to Interactive Programming in Python' course at coursera.org
#  made by Joe Warren, John Greiner, Stephen Wong, Scott Rixner

import simplegui

# define global variables
count = 0
game_num = 0
win_games = 0
timer_stop = False
result_of_game = ""

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global d_mil_sec
    
    b_sec = t // 10
    a_min = b_sec // 60
    c_ten_sec = b_sec % 60 
    d_mil_sec = t % 10   

    if c_ten_sec < 10:
        return str(a_min) + ":0" + str(c_ten_sec) + "." + str(d_mil_sec)
    else:
        return str(a_min) + ":" + str(c_ten_sec) + "." + str(d_mil_sec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_stop
    
    if timer_stop == False:
        timer.start()
        timer_stop = True
    
def stop():
    global timer_stop, game_num, win_games, d_mil_sec, result_of_game
    
    if timer_stop == True:
        timer.stop()
        
        if d_mil_sec != 0:
            game_num += 1
            timer.start()
            result_of_game = "Wrong!"
              
        if d_mil_sec == 0:
            game_num += 1
            win_games += 1
            timer.start()
            result_of_game = "Correct!"
            
def reset():
    global count, game_num, win_games, result_of_game, timer_stop
    
    if timer_stop == True:
        count = 0
        game_num = 0
        win_games = 0
        result_of_game = ""
        timer.stop()
        timer_stop = False

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    
    print count
    count += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(count)),[150, 110], 48, "Red")
    canvas.draw_text(str(game_num) + "/" + str(win_games),[320, 30], 32, "Green")
    canvas.draw_text(str(result_of_game),[10, 190], 32, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 400, 200)

# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()

# Andrii Shumylo 2015 (c)
