# the below commented code is only used to extract colors using colorgram package from the given image
#it can be commented and need not be run every time once we have got the color_list

#importing colorgram package from pypi
import colorgram

rgb_colors=[]

#extracting 30 colors from the image.jpg image file
colors = colorgram.extract('image.jpg', 30)

#looping through the colors returned by colorgram, extracting r,g,b values and adding it as a tuple into rgb_colors list
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

#this code gives us the rgb_colors list which is a set of tuples -> each tuple containing rgb values 
print(rgb_colors)

#the output of rgb_colors is copied from the terminal and pasted in a new list called as color_list. All the tuples with off white values have been removed

color_list =[ (204, 164, 107), (155, 73, 46), (52, 92, 123), (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), (163, 142, 158), (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90), (144, 21, 24), (41, 62, 74), (82, 145, 128), (181, 87, 89), (41, 66, 90), (13, 71, 68), (213, 178, 183), (179, 191, 207)]

import turtle 
import random


turtle.colormode(255)


t=turtle.Turtle()
t.penup()
t.hideturtle()
t.speed("fastest")

#this 3 lines is used to navigate the turtle from initial position to an appropriate starting point
t.setheading(225)
t.forward(300)
t.setheading(0)

number_of_dots=100


for dot_count in range(1,number_of_dots+1):
    t.dot(20,random.choice(color_list))#creating a dot of size 20 and a random color chosen from the color_list
    t.forward(50)

    #after every 10 dots, our turtle moves north 50 paces, then turns left and moves 500 paces, to the beginning of the line and then resets its heading to 0 degrees to prepare itself to draw the next line
    if dot_count%10==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



screen=turtle.Screen()
screen.exitonclick()