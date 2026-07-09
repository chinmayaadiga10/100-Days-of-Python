#drawing a square using turtle

from turtle import Turtle,Screen

tim=Turtle()

tim.shape("turtle")
tim.color("red")

#function to draw the square
def draw_square():
    for _ in range(4):#loop runs 4 times,each time prints a line for 100 paces and then turns right by 90degree
        tim.forward(100)
        tim.right(90)
        
draw_square()
    

screen=Screen()
screen.exitonclick()