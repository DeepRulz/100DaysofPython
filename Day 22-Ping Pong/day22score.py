from turtle import Turtle


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(x, y)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"{self.score}", False, "center", ("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", ("Arial", 24, "normal"))
