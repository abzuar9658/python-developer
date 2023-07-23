from game_screen import GameScreen
from snake import Snake

game_screen = GameScreen()

snake = Snake()
snake.add_body()
snake.add_body()
snake.add_body()
snake.add_body()
snake.add_body()

game_screen.listen(snake)
snake.move()
game_screen.listen(snake)
game_screen.hold_screen()
