#creating polygons -> triangle,square,pentagon,hexagon,heptagon,octagon,nonagon,decagon of randomly generated colors using turtle and random module

from turtle import Turtle,Screen
import random

tim=Turtle()
tim.pensize(3)

#list of colors from which the turtle will choose one using random module
#all of these colors are official turtle colors taken from the turtle documentation
colors=["red","blue","lawn green","cornflower blue","gold","coral","deep sky blue","light gray","yellow","orange"]


#function to generate a random color
def generate_random_color():
    color=random.choice(colors)
    return color

print(generate_random_color())

#function to generate shapes
def generate_shape(num_of_sides,color):
    tim.pencolor(color)
    angle=360/num_of_sides
    for _ in range(num_of_sides):
        tim.pendown()
        tim.right(angle)
        tim.forward(100)
        
#for loop used to print shapes from triangle to decagon
for num_of_sides in range(3,11):
    generate_shape(num_of_sides,generate_random_color())
        


screen=Screen()
screen.exitonclick()
    
    
#Unoptimized version of the same code ->
    
from turtle import Turtle,Screen

tim=Turtle()
tim.pensize(3)
tim.pencolor("red")

def generate_color():
    pass

for _ in range(4):
    tim.forward(100)
    tim.right(90)
tim.penup()
tim.forward(100)

tim.pendown()
for _ in range(5):
    tim.right(72)
    tim.forward(100)

for _ in range(6):
    tim.right(60)
    tim.forward(100)
    
for _ in range(7):
    tim.right(51.43)
    tim.forward(100)
    
for _ in range(8):
    tim.right(45)
    tim.forward(100)
    
for _ in range(9):
    tim.right(40)
    tim.forward(100)

for _ in range(10):
    tim.right(36)
    tim.forward(100)
    
    
screen=Screen()
screen.colormode(255)
screen.exitonclick()