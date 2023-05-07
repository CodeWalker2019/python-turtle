from constants import COLORS, DIRECTIONS
from turtle import Screen, Turtle
from helpers import move_toward_random_direction
import random

tim = Turtle()
tim.shape('turtle')
tim.pensize(15)
tim.speed('fastest')
screen = Screen()

for _ in range(50):
    tim.color(random.choice(COLORS))
    move_toward_random_direction(tim, DIRECTIONS)

screen.exitonclick()
