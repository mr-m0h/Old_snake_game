from turtle import Screen
import time
from scoreboard import ScoreBoard
from snake import Snake
from food import Food

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("My Snake Game")

snake = Snake()
food = Food()
board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    board.isvisible()

    # Detect collision with the wall

    if snake.segment[0].distance(food) < 15:
        food.random_place()
        snake.extend()
        board.increase_score()

    # Detect collision with the wall

    if snake.segment[0].xcor() > 290 or snake.segment[0].xcor() < -290 or snake.segment[0].ycor() > 290 or \
            snake.segment[0].ycor() < -290:
        board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segment:
        if segment == snake.segment[0]:
            pass
        elif snake.segment[0].distance(segment) < 10:
            board.reset()
            snake.reset()

    # if the head collides with any segment in the tail.
    # trigger game_over
screen.exitonclick()
