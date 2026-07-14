from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.initial_position()
        self.penup()
        self.shape("turtle")
        self.color("black")
        
    def initial_position(self):
        self.goto(STARTING_POSITION)
        
    def move_up(self):
        new_y=self.ycor()+10
        self.goto(x=0,y=new_y)
        
    def finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

