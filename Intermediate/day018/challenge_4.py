#generating a random walk activity -> 

import turtle as t
import random


tim=t.Turtle()
tim.pensize(15)
tim.speed(8)

#this line has to be used if colors are mentioned in terms of rgb values from 0 to 255
t.colormode(255)


colors=["red","blue","lawn green","cornflower blue","gold","coral","deep sky blue","light gray","yellow","orange"]


#function that is used to generate a random color from all rgb values. returns a tuple of rgb values
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

#list contains all the 4 directions in which the turtle moves, one chosen using random module
directions=[0,90,180,270]

#generating the random walk -> performs 300 iterations
for _ in range(300):
    tim.pencolor(random.choice(colors)) #pencolor set to random color generated from the colors list
    tim.pencolor(random_color())#pencolor set to a random color using the random_color function -> uses rgb values
    tim.setheading(random.choice(directions))#heading is set to a random heading from the directions list
    tim.forward(30)#the turtle is moved forward by 30 paces before repeating the entire process again
    



















screen=t.Screen()
screen.exitonclick()

