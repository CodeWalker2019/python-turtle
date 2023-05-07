import random


def get_random_color():
    return (
        random.uniform(0, 1),
        random.uniform(0, 1),
        random.uniform(0, 1),
    )


def draw_shape(turtle, number_of_sides):
    angle = round(360 / number_of_sides)
    for _ in range(number_of_sides):
        turtle.forward(30)
        turtle.right(angle)


def move_toward_random_direction(turtle, directions):
    random_direction = random.choice(directions)
    turtle.right(random_direction)
    turtle.forward(100)
