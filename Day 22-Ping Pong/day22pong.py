import time
from turtle import Screen, Turtle
from day22paddle import Paddle
from day22ball import Ball
from day22score import Score

screen = Screen()
score = Turtle()
score.hideturtle()
score.pu()
score.goto(0, 225)
score.color("white")
score.write("Score", False, "center", ("Arial", 24, "bold"))
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
paddle1score = Score(-200, 225)
paddle2score = Score(200, 225)
ball = Ball()
screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.a.ycor() >= 280 or ball.a.ycor() <= -280:
        ball.bounce()
    if ball.a.distance(paddle1.a) < 40 and ball.a.xcor() > 340:
        ball.xbounce()
    elif ball.a.distance(paddle2.a) < 40 and ball.a.xcor() < -340:
        ball.xbounce()
    if ball.a.xcor() > 360:
        paddle1score.increase()
        ball.reset()
    if ball.a.xcor() < -360:
        paddle2score.increase()
        ball.reset()

screen.exitonclick()
