import random
from turtle import Screen, Turtle
from helpers import get_random_color, draw_shape

tim = Turtle()
tim.speed(0)
tim.shape('turtle')
screen = Screen()
sides_count = 3

while True:
    tim.color(get_random_color())
    draw_shape(tim, sides_count)
    sides_count += 1
