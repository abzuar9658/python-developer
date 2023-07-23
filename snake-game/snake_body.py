import turtle

class SnakeBody():
  def __init__(self, next=None, prev=None, x_axis=0, y_axis=0, color='white', shape='square'):
    self.next = next
    self.prev = prev

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

  def set_position(self, pos):
    self.body.setpos(pos)

  def size(self):
    print('size', self.body.width())
    return self.body.pensize()

  def move_body(self, speed=10):
    self.body.forward(speed)
