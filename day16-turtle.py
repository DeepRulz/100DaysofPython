import turtle

Myturtle=turtle.Turtle()
Myturtle1=turtle.Turtle()
print(Myturtle)
Myturtle.shape("turtle")
Myturtle.color("aquamarine")
Myturtle1.shape("turtle")
Myturtle1.color("coral")

myscreen=turtle.Screen()
Myturtle.forward(100)
Myturtle1.right(180)
Myturtle1.forward(100)
myscreen.exitonclick()