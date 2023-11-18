# PossiblyAxolotl
# Background functions for my circular super hexagon clone
# -=-=-=-=-=-=-=-=-=-=-=-=-
# Started Nov 7, 2023
# Last updated Nov 9, 2023 

# all lists of points generated with the godot points converter
# to use it you can go into "single.tscn" in Godot and place the points wherever
# then on run it will copy the list to your clipboard

# same with "multi.tscn" but you have to make them the children of other nodes
# each child is an independent shape

import turtle
import random

current_background = 0
hearts = 3

# creating the drawing turtles
background_turtle = turtle.Turtle()
background_turtle.color("gray20")
background_turtle.hideturtle()

heart_turtle = turtle.Turtle()
heart_turtle.color("red")
heart_turtle.hideturtle()

text_turtle = turtle.Turtle()
text_turtle.color("white")
text_turtle.hideturtle()

def draw_title_text():
    text_turtle.clear()
    
    if current_background < 1:
        click_points = [[{"x":-28, "y":15},{"x":-44, "y":-0},{"x":-28, "y":-15},{"x":-44, "y":-0}],[{"x":-18, "y":15},{"x":-18, "y":-15},{"x":-2, "y":-15},{"x":-18, "y":-15}],[{"x":8, "y":15},{"x":8, "y":-15}],[{"x":34, "y":15},{"x":18, "y":-0},{"x":34, "y":-15},{"x":18, "y":-0}],[{"x":44, "y":15},{"x":44, "y":-0},{"x":60, "y":15},{"x":44, "y":-0},{"x":60, "y":-15},{"x":44, "y":-0},{"x":44, "y":-15}]]
        random_multi_draw(text_turtle, click_points, [2,2,2,2,2])
        turtle.ontimer(draw_title_text,t=100)

# heart drawing function
def draw_heart():
    heart_turtle.clear()

    if current_background != 0:
        heart_randomness = []
        colours = []

        # if a heart is alive make it bright and less random
        for i in range(hearts):
            heart_randomness.append(1)
            colours.append("red")
        
        # make all leftover hearts dark and more random
        while len(heart_randomness) < 3:
            heart_randomness.append(10)
            colours.append("darkred")

        # heart art
        heart_1_points = [{"x":-34, "y":287},{"x":-26, "y":294},{"x":-21, "y":286},{"x":-34, "y":274},{"x":-47, "y":286},{"x":-42, "y":294}]
        heart_2_points = [{"x":0, "y":287},{"x":8, "y":294},{"x":13, "y":286},{"x":0, "y":274},{"x":-13, "y":286},{"x":-8, "y":294}]
        heart_3_points = [{"x":34, "y":287},{"x":42, "y":294},{"x":47, "y":286},{"x":34, "y":274},{"x":21, "y":286},{"x":26, "y":294}]

        # draw hearts and loop
        random_multi_draw(heart_turtle, [heart_1_points, heart_2_points, heart_3_points], heart_randomness, colours)
        turtle.ontimer(draw_heart,t=100)
    
# background functions
def draw_background_square():
    if current_background == 1:
        background_turtle.clear()
        for i in range(9):
            i = round(i*1.7)+1
            points = [{"x":-20*i,"y":-20*i},{"x":-20*i,"y":0},{"x":-20*i,"y":20*i},{"x":0,"y":20*i},{"x":20*i,"y":20*i},{"x":20*i,"y":0},{"x":20*i,"y":-20*i},{"x":0,"y":-20*i}]
            random_draw(background_turtle, points, 3) 

        turtle.ontimer(draw_background_square,t=100)

def draw_background_grid():
    if current_background == 3:
        background_turtle.clear()
        points = [[{"x":-60, "y":60},{"x":60, "y":60},{"x":60, "y":-60},{"x":-60, "y":-60}],[{"x":120, "y":60},{"x":240, "y":60},{"x":240, "y":-60},{"x":120, "y":-60}],[{"x":-240, "y":60},{"x":-120, "y":60},{"x":-120, "y":-60},{"x":-240, "y":-60}],[{"x":-60, "y":-120},{"x":60, "y":-120},{"x":60, "y":-240},{"x":-60, "y":-240}],[{"x":120, "y":-120},{"x":240, "y":-120},{"x":240, "y":-240},{"x":120, "y":-240}],[{"x":-240, "y":-120},{"x":-120, "y":-120},{"x":-120, "y":-240},{"x":-240, "y":-240}],[{"x":-60, "y":240},{"x":60, "y":240},{"x":60, "y":120},{"x":-60, "y":120}],[{"x":120, "y":240},{"x":240, "y":240},{"x":240, "y":120},{"x":120, "y":120}],[{"x":-240, "y":240},{"x":-120, "y":240},{"x":-120, "y":120},{"x":-240, "y":120}]]
        random_multi_draw(background_turtle, points, [4,4,4,4,4,4,4,4,4])
        
        turtle.ontimer(draw_background_grid,t=100)

def draw_background_star():
    if current_background == 2:
        background_turtle.clear()
        for i in range(8):
            i = round(i*2)
            points = [{"x":-25*i,"y":-25*i},{"x":-20*i,"y":0},{"x":-25*i,"y":25*i},{"x":0,"y":20*i},{"x":25*i,"y":25*i},{"x":20*i,"y":0},{"x":25*i,"y":-25*i},{"x":0,"y":-20*i}]
            random_draw(background_turtle, points, 3) 

        turtle.ontimer(draw_background_star,t=100)

def draw_background_outline():
    if current_background == 0:
        background_turtle.clear()
        points = [{"x":-280,"y":-280},{"x":-280,"y":280},{"x":280,"y":280},{"x":280,"y":-280}]
        random_draw(background_turtle, points, 3) 

        turtle.ontimer(draw_background_outline,t=200)

def draw_background_death():
    if current_background == -1:
        background_turtle.clear()
        for i in range(10):
            points = [{"x":random.randint(-300,300),"y":random.randint(-300,300)},{"x":random.randint(-300,300),"y":random.randint(-300,300)},{"x":random.randint(-300,300),"y":random.randint(-300,300)},{"x":random.randint(-300,300),"y":random.randint(-300,300)}]
            random_draw(background_turtle, points, 3) 

        turtle.ontimer(draw_background_death,t=100)

# main drawing functions 
def random_draw(pen, points, randomness, closed=True):
    '''uses pen to draw the shape made of all the points (formatted {"x":0, "y":0}) in the table, and moves them based on the randomness'''
    pen.penup()
    
    # get starting point
    start_point = points[0]
    points.remove(start_point)
    
    # randomize starting point
    start_point["x"] += random.randrange(-randomness, randomness)
    start_point["y"] += random.randrange(-randomness, randomness)
    
    pen.goto(start_point["x"],start_point["y"])

    # randomize and draw each point
    pen.pendown()
    for point in points:
        pen.goto(point["x"]+random.randrange(-randomness, randomness),point["y"]+random.randrange(-randomness, randomness))
    
    # go back to the start if it should be a closed shape
    if closed:
        pen.goto(start_point["x"],start_point["y"])
        
    pen.penup()

def random_multi_draw(pen, points, randomness, colours = None):
    '''takes in a list of lists and draws all of them at once with the random draw function'''
    # loop through each list of points and random_draw them
    for counter in range(len(points)):
        point_list = points[counter]
        random_value = randomness[counter]
        if colours != None:
            pen.color(colours[counter])
        random_draw(pen, point_list, random_value)

# table of all background drawing funcs
background_process_functions = {
    -1:draw_background_death,
    1:draw_background_square,
    2:draw_background_star,
    3:draw_background_grid,
    0:draw_background_outline
}

# allows you to change the background easily
def update_background():
    background_process_functions[current_background]()

