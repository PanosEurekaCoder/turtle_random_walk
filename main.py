from turtle import Turtle, Screen
import random

colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
          "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
orientation = [0, 90, 180, 270]
melina = Turtle()
melina.pensize(4)
melina.speed(0)
my_screen = Screen()
boundary = 300

def random_walk(times):
    for _ in range(times):
        melina.color(random.choice(colors))
        melina.forward(25)
        x, y = melina.position()
        if abs(x) > boundary or abs(y) > boundary:
            melina.backward(25)  # Move back if out of boundary
            melina.setheading(random.choice(orientation))  # Change direction
        choice = random.choice(orientation)
        melina.setheading(choice)


times = int(input("how many times you want Melina to move?: "))

random_walk(times)
my_screen.exitonclick()

