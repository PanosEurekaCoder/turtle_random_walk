import turtle
from turtle import Turtle, Screen
import random

orientation = [0, 90, 180, 270]
melina = Turtle()
melina.pensize(4)
melina.speed(0)
my_screen = Screen()
boundary = 50
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


def random_walk(times):
    for _ in range(times):
        color_tuple = random_color()
        melina.color(color_tuple)
        melina.forward(25)
        x, y = melina.position()
        if abs(x) > boundary or abs(y) > boundary:
            melina.backward(12)  # Move back if out of boundary
            melina.setheading(random.choice(orientation))  # Change direction
        else:
            choice = random.choice(orientation)
            melina.setheading(choice)


times = int(input("how many times you want Melina to move?: "))
random_walk(times)
my_screen.exitonclick()

