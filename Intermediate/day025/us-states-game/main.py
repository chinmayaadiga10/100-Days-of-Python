import turtle
import pandas as pd

screen=turtle.Screen()
screen.title("U.S States game")
image="blank_states_img.gif"
screen.addshape(image)

#loading shape of turtle as background image
turtle.shape(image)


#Function to get the coordinates of the point in map, this is used to display the name of the state at the correct location
def get_mouse_click_coords(x,y):
    print(x,y)
    
turtle.onscreenclick(get_mouse_click_coords)




data=pd.read_csv("50_states.csv")
print(data)

states=data["state"].to_list()
print(states)

correct_guess=[]
score=0
game_state=True


while game_state:
    answer_state=screen.textinput(title=f"{len(correct_guess)}/50 states correct", prompt="What's another state's name ?").title()
    print(answer_state)
    if answer_state=="Exit":
        break
    if answer_state in states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data["state"]==answer_state]
        t.goto(x=state_data.x.item(),y=state_data.y.item())
        t.write(state_data.state.item())
        correct_guess.append(answer_state)
        states.remove(answer_state)
        score+=1
        print("Your guess is correct")
        if score==50:
            print("You've bossed the game")
            game_state=False
    else:
        print(f"Final score is : {score}")
        print("Wrong guess!")
        game_state=False
    

# generate a csv file that stores all the states which were not guessed by the user -> 

missed_states=[]
print(correct_guess)
print(states)
for state in states:
    if state not in correct_guess:
        missed_states.append(state)
print(missed_states)

missed_data=pd.DataFrame(missed_states)
missed_data.to_csv("states_to_learn.csv")

turtle.mainloop()
# screen.exitonclick()

