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
turtle.speed('fastest')

GAP_SIZE = 5

for angle in range(1, 360, GAP_SIZE):
    turtle.color(get_random_color())
    turtle.circle(100)
    turtle.setheading(angle)

screen = t.Screen()
screen.exitonclick()
