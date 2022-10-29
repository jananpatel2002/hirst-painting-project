###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

# Adding color tuples to a list
for color in colors:
    rgb_colors.append(color.rgb)

turtle.colormode(255)
timmy = turtle.Turtle()

# Filling colors and circles
timmy.penup()
timmy.setpos(-225, -225)
x_coordinate = timmy.xcor()
timmy.speed(0)
timmy.hideturtle()
for _ in range(10):
    for _ in range(10):
        color = (random.choice(rgb_colors))
        timmy.fillcolor(color)
        timmy.begin_fill()
        timmy.circle(20)
        timmy.end_fill()
        timmy.forward(50)
    timmy.setpos(x_coordinate, (timmy.ycor() + 50.0))


screen = turtle.Screen()
screen.exitonclick()
