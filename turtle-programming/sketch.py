import turtle

pen = turtle.Turtle()

screen = turtle.Screen()


def start_game():
    while True:
        turtle.forward(1)

def go_right():
    turtle.setheading(0)

def go_up():
    turtle.setheading(90)

def go_left():
    turtle.setheading(180)

def go_down():
    turtle.setheading(270)


screen.onkey(key='space', fun=start_game)
screen.onkey(key='w', fun=go_up)
screen.onkey(key='s', fun=go_down)
screen.onkey(key='d', fun=go_right)
screen.onkey(key='a', fun=go_left)

screen.listen()
screen.mainloop()