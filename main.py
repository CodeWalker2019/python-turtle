from constants import COLORS, DIRECTIONS
from turtle import Screen, Turtle
from helpers import draw_spirograph
import random

tim = Turtle()
tim.shape('turtle')
tim.speed('fastest')
draw_spirograph(turtle=tim, gap_size=5, colors=COLORS)

screen = Screen()
screen.exitonclick()
