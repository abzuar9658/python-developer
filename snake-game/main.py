from game_screen import GameScreen
from snake import Snake
from food import Food
from collision_detector import CollisionDetector

game_screen = GameScreen()
snake = Snake()
food = Food()

snake.add_body()

collision_detector = CollisionDetector(snake, food)
game_screen.listen(snake)
snake.move(collision_detector)
game_screen.listen(snake)
game_screen.hold_screen()
