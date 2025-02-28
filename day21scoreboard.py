from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.pu()
        self.goto(0, 250)
        self.update()
        self.hideturtle()
    def update(self):
        self.write(f"Score = {self.score}", False, "center", ("Arial", 24, "normal"))
    def increase(self):
        self.score+=1
        self.clear()
        self.update()