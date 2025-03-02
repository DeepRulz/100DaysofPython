from turtle import Turtle


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = Turtle("square")
        self.a.pu()
        self.a.color("White")
        self.a.shapesize(5, 1)
        self.a.setx(self.x)
        self.a.sety(self.y)

    def go_up(self):
        self.y = self.a.ycor() + 30
        if self.y>=280 or self.y<=-290:
            self.y=280
        self.a.goto(self.a.xcor(), self.y)


    def go_down(self):
        self.y = self.a.ycor() - 30
        self.a.goto(self.a.xcor(), self.y)
