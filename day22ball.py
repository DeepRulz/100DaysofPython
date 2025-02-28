import time
from turtle import Turtle


class Ball:
    def __init__(self):
        self.a = Turtle("circle")
        self.a.color("white")
        self.a.pu()
        self.xmove = 10
        self.ymove = 10
        self.speed = 1

    def move(self):
        newx = (self.a.xcor() + (self.xmove * self.speed))
        newy = (self.a.ycor() + (self.ymove * self.speed))
        self.a.goto(newx, newy)

    def bounce(self):
        self.ymove *= -1

    def xbounce(self):
        self.xmove *= -1
        self.speed *= 1.1

    def reset(self):
        time.sleep(0.5)
        self.a.goto(0, 0)
        self.speed = 1
