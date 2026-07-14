from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
        
    # this function is used to generate a new car 
    def create_car(self):
        #if this technique of creating a random variable is not used, then the cars are created every 0.1 second and it is impossible for the turtle to cross the screen
        random_chance=random.randint(1,6) # a random number generated between 1 and 6
        if random_chance==1: # new car created only if generated number is equal to 1
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(x=300,y=random_y)
            self.all_cars.append(new_car)
        
    # this function is used to move the cars in the screen
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
        
            
