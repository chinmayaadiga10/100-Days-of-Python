from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.display_score()
        
        
    def display_score(self):
        self.clear()
        self.goto(x=-220,y=250)
        self.write(f"Level : {self.level}", align="center", font=FONT)
        
    def update_score(self):
        self.level+=1
        self.display_score()
        

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER ! ", align="center", font=FONT)
        