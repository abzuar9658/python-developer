from snake_body import SnakeBody

class Snake():
  def __init__(self):
    self.head = SnakeBody()

  def add_body(self):
    new_body = SnakeBody(next_piece=self.head, x_axis=self.head.get_x() - 20, y_axis=self.head.get_y())
    self.head = new_body

  def move(self):
    while True:
      temp = self.head
      while temp:
        temp.move()
        temp = temp.next

  def set_listeners(self, angle):
    temp = self.head
    while temp.next:
      temp.body.setheading(angle)
      temp = temp.next

