STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player():
    def __init__(self):
        self.a=Turtle("turtle")
        self.a.pu()
        self.a.setheading(90)
        self.go_to_start()
    def up(self):
        self.a.forward(MOVE_DISTANCE)
    def go_to_start(self):
        self.a.goto(STARTING_POSITION)
    def is_at_finish_line(self):
        if self.a.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

