from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.fd(10)


def back():
    tim.bk(10)


def right():
    tim.right(10)


def left():
    tim.left(10)


def clear():
    tim.pu()
    tim.clear()
    tim.home()
    tim.pd()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
