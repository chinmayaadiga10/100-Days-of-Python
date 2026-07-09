#Technique 1 -> 

import turtle
tim=turtle.Turtle()

#Technique 2 ->

from turtle import Turtle
tim=Turtle()


# Technique 3 -> 
#avoid using this technique of importing using * -> as code increases, origin of method gets tough to track
from turtle import *


# Technique 4 -> 
#importing modules using alias technique

import turtle as t
timmy=t.Turtle()