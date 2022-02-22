from turtle import Turtle, colormode, done
colormode(255)
leo : Turtle = Turtle()
side_length: float = 300

leo.speed(50)
leo.hideturtle()

#leo.forward(50)
#leo.left(30)
#leo.right(40)
#leo.pencolor("pink")
#leo.fillcolor(32,67,93)
#leo.color("green", "yellow")

leo.color(220, 185, 253)
leo.penup()
leo.goto(45,60)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.hideturtle()
bob.color("purple")
leo.penup()
leo.goto(60,15)
leo.pendown()
bob.speed(100)

j: int = 0
while (j < 100):
    bob.forward(side_length)
    bob.left(122)
    side_length = side_length * 0.98
    j = j + 1

done()