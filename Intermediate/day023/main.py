import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")

game_state = True
while game_state:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with the car : 
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_state=False
            
    # Detect a successful crossing : 
    if player.finish_line():
        player.initial_position() #moves the player turtle back to the starting position
        car_manager.level_up()
        scoreboard.update_score()
            
    


screen.exitonclick()