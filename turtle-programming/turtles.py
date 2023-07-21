import random
import turtle
turtle.colormode(255)

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

turtle = turtle.Turtle()
shapes = 10
sides = 10
size = 100

for _ in range(shapes):
    turtle.fillcolor(random_color())
    turtle.begin_fill()

    for _ in range(sides):
        turtle.forward(size)
        turtle.right(360/sides)

    turtle.end_fill()
    turtle.penup()  
    turtle.setpos((turtle.xcor() + 10, turtle.ycor() - 10))
    turtle.pendown()
    size  = size - 20
    sides = sides - 1


