# etch a sketch project -> drawing on screen using event listeners in turtle

from turtle import Turtle,Screen

t=Turtle()

def move_forward():
    t.setheading(0)
    t.forward(30)
    
def move_clockwise():
    new_heading=t.heading()-10
    t.setheading(new_heading)
    t.forward(30)

def move_anticlockwise():
    t.left(10)
    t.forward(30)

def move_backward():
    t.setheading(0)
    t.backward(30)
    
def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen=Screen()
screen.listen()

screen.onkey(key="d",fun=move_forward)
screen.onkey(key="a",fun=move_backward)
screen.onkey(key="w",fun=move_clockwise)
screen.onkey(key="s",fun=move_anticlockwise)

screen.onkey(key="c",fun=clear_screen)

screen.exitonclick()
