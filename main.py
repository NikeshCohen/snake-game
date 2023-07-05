from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
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

# Event Listeners
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

playing = True

# Initialization of the game
while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.update_score()
        food.color(food.random_color())

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        playing = False
        scoreboard.end_game()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            playing = False
            scoreboard.end_game()
screen.exitonclick()
