from snake_body import SnakeBody

class Snake():
  def __init__(self):
    self.head = SnakeBody()
    self.tail = self.head

  def add_body(self):
    new_body = SnakeBody(x_axis=self.tail.get_x() - 20, y_axis=self.tail.get_y())
  
    if self.head.next == None:
      self.tail = new_body
      self.tail.prev = self.head
      self.head.next = self.tail
      return

    new_body.prev = self.tail
    self.tail.next = new_body
    self.tail = new_body

  def move(self):
    while True:
      current_position = self.head.get_position()
      self.head.move_body()
  
      temp = self.head.next
      while temp:
        curr = temp.prev.get_position()
        temp.set_position(current_position)

        print('curr', curr)
        print('current pos', current_position)

        current_position = curr

        temp = temp.prev

  def set_listeners(self, angle):
    self.head.body.setheading(angle)

