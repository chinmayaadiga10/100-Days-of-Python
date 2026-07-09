#drawing a dashed line using turtle module

import turtle

t=turtle.Turtle()

for _ in range(15):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(10)


screen=turtle.Screen()
screen.exitonclick()