import colorgram
import turtle as t
import random

colors = colorgram.extract('painting.webp', 30)

rgb_colors = []

for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    rgb_colors.append((red, green, blue))

t.colormode(255)
t.penup()
t.hideturtle()
t.speed("fastest")

t.setx(-270)
t.sety(-270)

for dot_count in range(1, 101):
    random_color = random.choice(rgb_colors)

    t.dot(20, random_color)
    t.forward(50)

    if dot_count % 10 == 0:
        t.sety(t.ycor() + 50)
        t.setx(-270)

screen = t.Screen()
screen.exitonclick()
