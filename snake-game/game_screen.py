from turtle import Screen

class GameScreen():
  def __init__(self):
    self.screen = Screen()
    self.screen.title('Welcome to Snake Game')
    self.screen.setup(width=600, height=600)
    self.screen.bgcolor('black')

  def hold_screen(self):
    self.screen.exitonclick()

  def listen(self, snake):
    self.screen.listen()
    self.screen.onkey(lambda: snake.set_listeners(90), 'Up')
    self.screen.onkey(lambda: snake.set_listeners(180), 'Left')
    self.screen.onkey(lambda: snake.set_listeners(0), 'Right')
    self.screen.onkey(lambda: snake.set_listeners(270), 'Down')