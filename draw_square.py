from turtle import *
# length = int(input("length:"))
# color_square = (input("color: "))
speed(-1)
def draw_square(length,color_square):
    for i in range (4) :
        color(color_square)
        forward ( length )
        left (90)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()