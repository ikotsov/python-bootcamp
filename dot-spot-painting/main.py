import turtle as t
import random

t.colormode(255)


def get_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = (red, green, blue)
    return random_color


turtle = t.Turtle()
turtle.pensize(15)

orientation = [0, 90, 180, 270]

for _ in range(200):
    turtle.color(get_random_color())
    turtle.setheading(random.choice(orientation))
    turtle.forward(30)
