import random
import turtle
from turtle import *
gameon=False
screen = Screen()
screen.setup(500,400)
turtles=["red","orange","yellow","green","blue","violet"]
turtle1=[]
winner=turtle.textinput("Winner","Who do you think will win the race?")
a=-75
if winner:
    gameon=True
for turt in turtles:
    colour=turt
    turt=Turtle()
    turt.pu()
    turt.color(colour)
    turt.pencolor(colour)
    turt.shape("turtle")
    turt.goto(-230,a)
    a+=30
    turtle1.append(turt)
win=""

while gameon==True:

    for e in turtle1:
        if e.xcor()>230:
            gameon = False
            winning_color = e.pencolor()
            if winning_color == winner:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        e.fd(random.randint(0,10))




