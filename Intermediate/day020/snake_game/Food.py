#importing turtle to create food and random module to create food at random location
from turtle import Turtle 
import random

#main food class which creates the food and inherits properties from turtle class
class Food(Turtle):
    
    def __init__(self):
        super().__init__() 
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    #refresh method creates food and places at specified random location in the screen
    def refresh(self):
        random_x=random.randint(-270,270)
        random_y=random.randint(-270,270)
        self.goto(x=random_x,y=random_y)