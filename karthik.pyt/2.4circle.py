import turtle

def draw_circle(t, color):
    t.color(color)
    t.pensize(20)
    t.down()
    t.circle(60)
    t.up()
    t.backward(100)

def main():
    t = turtle.Turtle()

    colors = ['red', 'green', 'blue']
    t.up()
    t.goto(200, 0)

    for color in colors:
        draw_circle(t, color)

    turtle.done()

if __name__ == "__main__":
    main()


