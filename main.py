# PossiblyAxolotl
# Turtle loop project
# Circular super hexagon clone https://terrycavanagh.itch.io/super-hexagon
# -=-=-=-=-=-=-=-=-=-=-=-=-
# Started Nov 1, 2023
# Last updated Nov 10, 2023 

from scripts.othermath import *
import scripts.input as input
import scripts.wobble as wobble
import turtle
import random

# define constants
SCREEN_SIZE = 600
MAX_DISTANCE = SCREEN_SIZE/4
MAX_8BIT = 1023

ACCELEROMETER_DEADZONE = 25

WALL_THICKNESS = 10
BACKGROUND_RANDOMNESS = 4

walls = []

state_machine = "title"

# wall variables
wall_shrink_speed = 1000
wall_close_speed = 0.004
wall_turn_speed = 80

# register cursor image as shapes
turtle.register_shape("images/player.gif")

# window setup
wn = turtle.Screen()
wn.setup(SCREEN_SIZE,SCREEN_SIZE) # set screen size
wn.title("CLICK")
canvas = wn.getcanvas()
canvas.config(cursor="none") # hide mouse cursor
canvas._rootwindow.resizable(False, False) # disable resizing window
wn.bgcolor("black")
wn.tracer(60)

# player setup
player = turtle.Turtle()
player.speed(0)
player.color("blue")
player.shape("images/player.gif")
player.penup()

# middle turtle setup - used to figure out the angle to the player
mid_turtle = turtle.Turtle()
mid_turtle.color("blue")
mid_turtle.speed(0)
mid_turtle.penup()
mid_turtle.hideturtle()

# circle turtle setup - used to draw walls
circle_turtle = turtle.Turtle()
circle_turtle.penup()
circle_turtle.color("white")
circle_turtle.speed(0)
circle_turtle.hideturtle()

# allows you to create walls
def add_wall(angle, opening, shrink_speed, close_speed, turn_speed):
    walls.append({"radius":SCREEN_SIZE/1.35,"angle":angle,"opening":opening,"hit":False,"shrink_speed":shrink_speed,"close_speed":close_speed,"turn_speed":turn_speed})

def random_wall():
    add_wall(random.randint(0,359), random.randint(50,90), wall_shrink_speed/1000, wall_close_speed, random.randrange(-wall_turn_speed,wall_turn_speed)/100)

# draws a circular wall
def draw_wall(drawing_turtle, radius, angle, opening):
    drawing_turtle.goto(0,0)
    drawing_turtle.seth(angle)
    drawing_turtle.fd(radius)
    drawing_turtle.left(90)
    drawing_turtle.pendown()
    drawing_turtle.circle(radius,360-opening,20)
    drawing_turtle.penup()

# go to title screen
wobble.current_background = 0
wobble.update_background()
wobble.draw_title_text()

# map click to start the game and go to title
def left_click(x,y):
    global state_machine, wall_shrink_speed, wall_turn_speed
    if state_machine == "title":
        state_machine = "game"
        wobble.current_background = random.randint(1,3)
        wobble.update_background()
        wobble.hearts = 3
        wobble.draw_heart()

        wall_shrink_speed = 1000
        wall_turn_speed = 10

        random_wall()
    if state_machine == "death":
        state_machine = "title"
        wobble.current_background = 0
        wobble.update_background()

turtle.listen()
turtle.onscreenclick(left_click)

# mainloop
while True:
    canvas = turtle.getcanvas()

    # get input from mouse
    play_x, play_y = input.get_mouse_pos(canvas, SCREEN_SIZE, SCREEN_SIZE)
    
    # clamp player input to stay on screen, accounting for the player's sprite
    play_x = clamp(play_x, -SCREEN_SIZE/2+10, SCREEN_SIZE/2-16)
    play_y = clamp(play_y, -SCREEN_SIZE/2+16, SCREEN_SIZE/2-10)
  
    # move player
    player.goto(play_x, play_y)
    
    if state_machine == "game":
        # turn the middle turtle towards the player
        mid_turtle.seth(mid_turtle.towards(play_x, play_y))

        # clear old walls
        circle_turtle.clear()

        for wall in walls: # was planning to have multiple walls, was too laggy
            # wall movement
            wall["radius"] -= wall["shrink_speed"]
            wall["opening"] -= wall["close_speed"]
            wall["angle"] -= wall["turn_speed"]
            
            # make the wall angle loop
            if wall["angle"] > 359:
                wall["angle"] -= 359
            elif wall["angle"] < 0:
                wall["angle"] += 359
            
            # wall drawing
            if wall["hit"]:
                circle_turtle.color("red")
            else:
                circle_turtle.color("white")
            draw_wall(circle_turtle, wall["radius"], wall["angle"], wall["opening"])
            
            # collision detection
            player_distance = mid_turtle.distance(play_x, play_y)
            if between(player_distance, wall["radius"]-WALL_THICKNESS, wall["radius"]+WALL_THICKNESS) and not between_circle_doorway(mid_turtle.heading(), wall["angle"]-wall["opening"], wall["angle"], wall["opening"]):
                if not wall["hit"]: # if you touch a wall that isn't red
                    wobble.hearts -= 1
                    wall["hit"] = True

                    if wobble.hearts < 1: # if you're out of health show death screen
                        wobble.current_background = -1
                        wobble.update_background()
                        walls = []

                        state_machine = "death"

                        circle_turtle.clear()

                        wobble.draw_title_text()

                        break
            
            # removing small walls
            if wall["radius"] < 0:
                walls.remove(wall)

                # slowly increase values
                if wall_shrink_speed < 1200:
                    wall_shrink_speed += 5
                if wall_turn_speed < 65:
                    wall_turn_speed += 1

                random_wall() # create new wall
        #wall_loop()

#exit when the loop is exited
exit()