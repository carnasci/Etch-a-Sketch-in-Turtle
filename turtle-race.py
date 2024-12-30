from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make guess", prompt="Which Turtle will win the race? Choose a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


# y_start = -80
# for color in colors:
#
#     for turtle in turtles:
#         turtle = Turtle(shape="turtle")
#     turtle.color(color)
#     turtle.penup()
#     turtle.goto(x=-230, y=y_start)
#     y_start += 30

race_is_on = False
y_start = -80
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_start)
    turtles.append(new_turtle)
    y_start += 30

if user_guess:
    race_is_on = True

while race_is_on:

    for turtle in turtles:
        if turtle.xcor() == 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've Won! The {winning_color} turtle has won.")
            else:
                print(f"You've Lost! The {winning_color} turtle has won.")
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)

screen.exitonclick()