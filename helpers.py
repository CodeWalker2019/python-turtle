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


def draw_spirograph(turtle, gap_size, colors=None):
    for _ in range(round(360 / gap_size)):
        if colors:
            turtle.color(random.choice(colors))
        turtle.setheading(turtle.heading() + gap_size)
        turtle.circle(100)
