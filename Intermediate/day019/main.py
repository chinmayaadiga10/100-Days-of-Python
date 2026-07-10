# understanding the usage of event listeners in turtle module ->

from turtle import Turtle,Screen

t=Turtle()

def move_forward():
    t.forward(10)

screen=Screen()

screen.listen()
screen.onkey(key="space",fun=move_forward)

screen.exitonclick()