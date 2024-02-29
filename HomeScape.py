#introductory message:
print('Welcome to My Beautiful Living Solutions')

# File: HomeScape.py
# By Melkamu Gebre
# Description of Program: Use turtle graphics to design a HomeScape in Python

import turtle

# Drawing flowers and rods
def draw_flower(x, y):
    turtle.fillcolor('deeppink2')
    turtle.begin_fill()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for _ in range(5):   
        turtle.circle(30, 180)
        turtle.right(108)   
    turtle.penup()

    turtle.end_fill()
    turtle.up()
    turtle.goto(270, -70)
    turtle.down()
    turtle.color('black')
    turtle.dot(30)

def draw_rod(x):
    turtle.right(77)
    turtle.fd(x)
    turtle.right(180)
    turtle.fd(80)
    turtle.fillcolor('blue')

def draw_second_flower(x, y):
    turtle.begin_fill()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(5):  
        turtle.circle(30, 180)
        turtle.right(108)

    turtle.penup()
    turtle.end_fill()
    turtle.up()
    turtle.goto(-270, -80)
    turtle.down()
    turtle.color('black')
    turtle.dot(30)

def draw_rod2(x):
    turtle.right(200)
    turtle.fd(x)
    turtle.fillcolor('blue')
    turtle.penup()
    turtle.end_fill()
    turtle.up()
    turtle.goto(-270, -80)
    turtle.down()
    turtle.color('black')
    turtle.dot(30)

# Import turtle as t
t = turtle.Turtle()
scr = turtle.getscreen()
scr.bgcolor("SkyBlue1")

# Drawing the body of the house
def draw_body(x, y): 
    t.speed(10)
    t.penup()
    t.pensize(3)
    t.color("black", "brown1")
    t.begin_fill()
    t.goto(x, y)
    t.pendown()
    t.forward(400)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.end_fill()

    # Drawing partition
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.end_fill()

    # Drawing roof
    t.color("black", "gray")
    t.begin_fill()
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.end_fill()
    t.begin_fill()
    t.backward(100)
    t.left(60)
    t.forward(300)
    t.right(60)
    t.forward(100)
    t.end_fill()

# Drawing door
def draw_door(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color("black", "lightsalmon3")
    t.forward(230)
    t.left(90)
    t.begin_fill()
    t.forward(90)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.penup()
    t.goto(40, -100)
    t.dot(10)
    t.color('brown1')
    t.pendown()

# Drawing the left window
def draw_left_window(x, y):
    t.penup
    t.goto(x, y)
    t.pendown()
    t.color("black", "cornflowerblue")
    t.begin_fill()
    t.backward(50)
    t.left(90)
    t.begin_fill()
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(60)
    t.end_fill()
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(60)
    t.backward(30)
    t.right(90)
    t.forward(25)
    t.backward(50)
    t.end_fill()

# Drawing the right window
def draw_right_window(x, y):
    t.penup()
    t.setheading(270)
    t.goto(x, y)
    t.pendown()
    t.color("black", "cornflowerblue")
    t.backward(50)
    t.begin_fill()
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.end_fill()
    t.forward(60)
    t.backward(30)
    t.right(90)
    t.forward(25)
    t.backward(50)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.penup()

# Drawing grass
def draw_grass(x, y):
    t.color("black", "green")
    t.goto(x, y)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.forward(1300)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(1300)
    t.right(90)
    t.forward(180)
    t.end_fill()
    t.penup()

# Drawing the circle of the sun
def draw_circle_sun(x, y):
    t.goto(x, y)
    t.pendown()
    t.color("yellow", "yellow")
    t.begin_fill()
    t.circle(45)
    t.end_fill()
    t.goto(-210, 255)

    # Drawing sunrays
    t.pensize(5)
    for _ in range(12):
        t.forward(80)
        t.backward(80)
        t.left(30)
    t.penup()   

# Drawing clouds
def draw_clouds(x, y):
    
    t.goto(350, 260)
    t.pendown()
    t.color("white", "white")
    t.setheading(90)
    t.begin_fill()
    t.circle(60, 180)
    t.end_fill()
    t.goto(x, y)
    t.setheading(90)
    t.begin_fill()
    t.circle(80, 180)
    t.end_fill()
    t.goto(90, 260)
    t.pendown()
    t.color("white", "white")
    t.setheading(90)
    t.begin_fill()
    t.circle(60, 180)
    t.end_fill()

# Calling functions
draw_body(-200, -150)
draw_door(-200, -150)
draw_left_window(-60, -50)
draw_right_window(100, -50)
draw_grass(-650, -150)
draw_circle_sun(-160, 260)
draw_clouds(235, 260)
draw_flower(310, -100)
draw_rod(265)
draw_second_flower(-250, -30)
draw_rod2(250)

turtle.done()
