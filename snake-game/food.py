from turtle import Turtle
import random

class Food():
    def __init__(self):
        self.body = Turtle()
        self.body.setpos((random.randint(10,300), random.randint(10,300)))
        self.body.color('red')
        self.body.penup()
        self.body.shape('circle')

    def change_position(self):
        self.body.setpos((random.randint(-300,300), random.randint(-300,300)))
    
    def get_position(self):
        return self.body.position()

    def get_size(self):
        return self.body.pensize()