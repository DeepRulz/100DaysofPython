import time
from turtle import Screen
from day20snake import Snake
from day21food_cnt20 import Food
from day21scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Rabbit Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
gameon = True
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()
while gameon == True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.mainturt.distance(food) < 25:
        food.refresh()
        score.increase()
        snake.extend()
    if snake.mainturt.xcor() > 300 or snake.mainturt.xcor() < -300 or snake.mainturt.ycor() > 300 or snake.mainturt.ycor() < -300:
        gameon = False
        score.gameover()
    for seg in snake.turtles:
        if seg == snake.mainturt:
            pass
        elif snake.mainturt.distance(seg) < 10:
            gameon = False
            score.gameover()

screen.exitonclick()
