import turtle

class SnakeBody():
  def __init__(self, next_piece=None, x_axis=0, y_axis=0, color='white', shape='square'):
    print(x_axis, y_axis)
    self.next = next_piece
    self.body = turtle.Turtle()
    self.body.penup()
    self.body.setpos(x_axis, y_axis)
    self.body.color(color)
    self.body.shape(shape)

  def get_position(self):
    return self.body.position()

  def get_x(self):
    return self.body.xcor()

  def get_y(self):
    return self.body.ycor()

  def size(self):
    print('size', self.body.width())
    return self.body.pensize()

  def move(self, speed=10):
    self.body.forward(speed)
