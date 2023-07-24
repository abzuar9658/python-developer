from snake_body import SnakeBody

class Snake():
  def __init__(self):
    self.head = SnakeBody()
    self.tail = self.head

  def add_body(self, color='white'):
    new_body = SnakeBody(x_axis=self.tail.get_x() - 20, y_axis=self.tail.get_y(), color=color)
  
    if self.head.next == None:
      self.tail = new_body
      self.tail.prev = self.head
      self.head.next = self.tail
      return

    new_body.prev = self.tail
    self.tail.next = new_body
    self.tail = new_body

  def move(self, collision_detector):
    while True:
      # logic is based on linkedlist iteration with next following the prev
      # head moves and rest follow their prevs
      temp = self.head

      prev_temp_position = temp.get_position()
      temp.move_body() # start moving head, rest will just follow
      collision_detector.detect_food_to_snake_collision()
      temp = temp.next

      while temp:
        curr_temp_pos = temp.get_position()
        temp.set_position(prev_temp_position)
        prev_temp_position = curr_temp_pos
        temp = temp.next

  def get_position(self):
    return self.head.get_position()

  def get_size(self):
    return self.head.get_size()
  
  def set_listeners(self, angle):
    self.head.body.setheading(angle)

