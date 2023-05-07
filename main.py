import random
from turtle import Screen, Turtle
from helpers import get_random_color, move_toward_random_direction

tim = Turtle()
tim.shape('turtle')
screen = Screen()
directions = (0, 270, 180, 90)

while True:
    tim.color(get_random_color())
    move_toward_random_direction(tim, directions)
