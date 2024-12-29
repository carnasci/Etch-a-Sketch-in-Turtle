from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

def move_forwards():
    return tim.fd(10)

def move_backwards():
    return tim.backward(10)

def turn_left():
    return tim.left(5)

def turn_right():
    return tim.right(5)

def reset():
    return tim.reset()

my_screen.listen()
my_screen.onkey(move_forwards, "w")
my_screen.onkey(move_backwards, "s")
my_screen.onkey(turn_left, "a")
my_screen.onkey(turn_right, "d")
my_screen.onkey(reset, "c")
my_screen.exitonclick()