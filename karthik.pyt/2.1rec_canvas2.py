class Canvas:
    def draw(self,cont):
        print(cont)

class Rect:
    def __init__(self,width,heit):
        self.width = width
        self.heit = heit
def draw_rectangle(canvas,rect):
        for i in range(rect.heit):
            line = '-'*rect.width
            canvas.draw(line)
canvas = Canvas()
rect = Rect(10,4)
draw_rectangle(canvas,rect)

