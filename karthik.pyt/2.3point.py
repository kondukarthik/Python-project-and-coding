import turtle

def draw_circle(radius):
    for i in range(360):
        turtle.forward(radius)
        turtle.left(1)


draw_circle(1)
turtle.done()
