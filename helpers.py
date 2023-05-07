import random


def get_random_color(colours = None):
    if colours:
        min_random_number = 0
        max_random_number = len(colours) - 1
        random_index = random.randint(min_random_number, max_random_number)
        return colours[random_index]

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
    directions_count = len(directions)
    random_direction = directions[random.randint(0, directions_count - 1)]
    turtle.right(random_direction)
    turtle.forward(100)
