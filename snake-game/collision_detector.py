class CollisionDetector():
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        self.score = 0

    def detect_food_to_snake_collision(self):
        if self.__detected_collision():
            self.score += 1
            self.snake.add_body()
            self.food.change_position()

    def __detected_collision(self):
        snake_x, snake_y = self.snake.get_position()
        food_x, food_y = self.food.get_position()

        snake_size = self.snake.get_size() * 10 # 10 is the distance from center to each side if size is 20
        food_size = self.food.get_size() * 10 # 10 is the distance from center to each side if size is 20

        if (abs((snake_x + snake_size) - (food_x + food_size)) < 10 and abs((snake_y + snake_size) - (food_y + food_size)) < 10):
            return True 

        return False



