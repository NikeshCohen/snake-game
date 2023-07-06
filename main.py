from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
from game import Status
import time

# Screen Specifications
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating the snake from the Snake object
snake = Snake()

# Creating the food from the Food object
food = Food()

# Creating the scoreboard from the Scoreboard object
scoreboard = Scoreboard()
scoreboard.update_score()

# Creating the game state from Status object
game_state = Status()

# Event Listeners
screen.listen()

# Up
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_up, "w")

# Down
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_down, "s")

# Left
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_left, "a")

# Right
screen.onkeypress(snake.move_right, "Right")
screen.onkeypress(snake.move_right, "d")

screen.onkeypress(game_state.end_game, "q")


# Initialization of the game
while game_state.playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        food.color(food.random_color())

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
