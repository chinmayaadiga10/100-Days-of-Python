from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)#this tracer method controls the animation in screen, value 0 turns off the animation
#when animation is turned off, the screen has to be manually updated and refreshed every time

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")


screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_state=True
while game_state:
    time.sleep(ball.move_speed)#while loop sleeps for 0.1 before again the move method is called
    screen.update() #this is used as the animation is set to 0 using the tracer method
    ball.move()
    
    #detect collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        #the ball needs to bounce in this situation
        ball.bounce_y()
        
    #detect collision with the paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
        
    #detect when right paddle misses the ball
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.left_point()
        
        
    #detect left side paddle miss
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.right_point()


screen.exitonclick()