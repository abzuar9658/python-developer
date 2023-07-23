import turtle
import random
import numpy as np

turtle.colormode(255)
turtle.screensize(canvwidth=200, canvheight=200)
screen = turtle.Screen()

def random_color():
    rgbl= list(np.random.choice(range(256), size=3))
    return tuple(rgbl)

turtle_count = turtle.textinput("Welcome to turtlys", "How many turtles for the race?(Max 10): ")


def set_y_position(number, count, alterantor):
    if number == 0:
        return 0, count, alterantor
    else:
        distance = alterantor * 50 * (1 if number % 2 == 0 else -1)
        count = count + 1
        if count - alterantor >= 2:
            alterantor += 1
            count -=1

        return distance, count, alterantor


count = 1
alterantor = 1
turtleys = []
for i in range(min(int(turtle_count), 10)):
    turtley = turtle.Turtle(shape='turtle')
    turtley.color(random_color())
    turtley.penup()
    distance, count, alterantor = set_y_position(i, count, alterantor)
    turtley.goto(-300, distance)
    turtleys.append(turtley)

while True:
    won = False
    for turtly in turtleys:
        turtly.forward(random.randint(3,10))
        print(turtly.xcor())
        if turtly.xcor() == 320:
            print('Tutle won')
            won = True
            break
    if won:
        break


screen.mainloop()