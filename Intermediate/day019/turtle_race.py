# turtle race project where in the user can place his bet

from turtle import Turtle,Screen
import random


screen=Screen()

#specifying height and width of the screen. Turtle created at (0,0) which is the center of the screen
screen.setup(width=500,height=400)

colors=["red","orange","yellow","green","blue","purple"]

#indicates the positions that will be occupied by new instances of class Turtle
y_positions=[-70,-40,-10,20,50,80]

race_turtles=[]


#method used to prompt user to enter text, user input stored in variable user_bet
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color :")
print(user_bet)



#creating 6 turtle instances from turtle class for turtle race
for turtle_index in range(0,6):
    t=Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230,y=y_positions[turtle_index])#specifying the position of each turtle that is created
    race_turtles.append(t)
    
race_state=False

if user_bet:
    race_state=True

while race_state:
    for turtle in race_turtles:
        if turtle.xcor()>230:
            race_state=False
            win_color=turtle.pencolor()
            if win_color==user_bet:
                print(f"Congratulations! You're {user_bet} turtle has won the race")
            else:
                print(f"You've lost. {win_color} turtle is the winner")
        random_distance=random.randint(0,10)#moving the turtle by a random distance
        turtle.forward(random_distance)
    

screen.exitonclick()