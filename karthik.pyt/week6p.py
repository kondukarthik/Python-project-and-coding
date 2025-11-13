import turtle
t=turtle.Turtle()
list1=["orange","yellow","red","blue"]
def draw_point(point_size):
    t.up()
    t.goto(200,0)
    for i in range(4):
        t.down()
        t.color(list1[i])
        t.pensize(20)
        t.circle(60)
        t.up()
        t.backward(100)
        t.speed(1)
draw_point(20)
turtle.done()