from turtle import Turtle

turtle = Turtle()


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        turtle.right(angle)
        turtle.forward(100)


for num_of_sides in range(3, 11):
    draw_shape(num_of_sides)
