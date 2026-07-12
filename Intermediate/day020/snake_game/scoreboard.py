from turtle import Turtle

with open("data.txt")as file:
    content=file.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score=0 #used to keep track of the score -> starts at 0
        self.high_score=(int)(content)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=270)
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}",align='center', font=('Courier', 24, 'normal'))
        
    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w")as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()
        
    #this function is not used after we refactor the coe and try to implement the high score functionality
    # def game_over(self):
    #     self.goto(0,0)#message should be displayed at the center of the screen
    #     self.write(f"Game over !",align='center', font=('Courier', 24, 'normal'))
    
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
    