import turtle
t = turtle.Turtle()
for i in range(4):
    t.begin_fill()
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.fillcolor("red")
    t.end_fill()
turtle.done()
