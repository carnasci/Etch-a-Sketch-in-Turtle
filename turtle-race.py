from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make guess", prompt="Which Turtle will win the race? Choose a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = ["red", "orange", "yellow", "green", "blue", "purple"]


# y_start = -80
# for color in colors:
#
#     for turtle in turtles:
#         turtle = Turtle(shape="turtle")
#     turtle.color(color)
#     turtle.penup()
#     turtle.goto(x=-230, y=y_start)
#     y_start += 30

y_start = -80
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_start)
    y_start += 30

screen.exitonclick()