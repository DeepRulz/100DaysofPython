from turtle import Turtle
STARTING = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.turtles=[]
        self.create_Snake()
        self.mainturt=self.turtles[0]

    def create_Snake(self):
        for start in STARTING:
            self.addseg(start)

    def addseg(self,start):
        s = Turtle("square")
        s.color("white")
        s.pu()
        s.goto(start)
        self.turtles.append(s)
    def extend(self):
        self.addseg(self.turtles[-1].position())
    def move(self):
        for seg in range(len(self.turtles) - 1, 0, -1):
            newx = self.turtles[seg - 1].xcor()
            newy = self.turtles[seg - 1].ycor()
            self.turtles[seg].goto(newx, newy)
        self.mainturt.fd(MOVE_DISTANCE)
    def up(self):
        if self.mainturt.heading()!=DOWN:
            self.mainturt.setheading(90)
    def down(self):
        if self.mainturt.heading() != UP:
            self.mainturt.setheading(270)
    def left(self):
        if self.mainturt.heading() != RIGHT:
            self.mainturt.setheading(180)
    def right(self):
        if self.mainturt.heading() != LEFT:
            self.mainturt.setheading(0)
