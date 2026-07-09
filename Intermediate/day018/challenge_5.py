#drawing a spirograph 

import turtle as t
import random


tim=t.Turtle()
# tim.pensize(15)
tim.speed("fastest")

t.colormode(255)

#function to generate random color and return the color as a tuple
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

#drawing initial circle of radius 100 paces
tim.circle(100)

#main function that is used to draw the spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)
        
#calling the function with size of gap equal to 5 degrees -> loop runs 360/5=72 times
draw_spirograph(3)



screen=t.Screen()
screen.exitonclick()

