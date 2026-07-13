#this file contains the main.py file that was created before the main.py file was refactored and paddle class was created

#the sole purpose of this file is to help me with understanding the concepts

from turtle import Turtle,Screen

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
#this tracer method controls the animation in screen, value 0 turns off the animation
#when animation is turned off, the screen has to be manually updated and refreshed every time

paddle=Turtle()
paddle.shape("square")
paddle.color("white")
paddle.penup()
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.goto(x=350,y=0)

def go_up():
    new_y=paddle.ycor()+20
    paddle.goto(x=paddle.xcor(),y=new_y)
    
def go_down():
    new_y=paddle.ycor()-20
    paddle.goto(x=paddle.xcor(),y=new_y)


screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")


game_state=True
while game_state:
    screen.update() #this is used as the animation is set to 0 using the tracer method


screen.exitonclick()