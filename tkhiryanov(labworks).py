import turtle
turtle.shape('turtle')


def square_in_square(side, number_of_squares):
    """draw square
    side = first size of the edge"""
    for a in range(1, number_of_squares + 1):
        for i in range(4):
            turtle.left(90)
            turtle.forward(side * a)
        turtle.penup()
        turtle.forward(side * 0.5)
        turtle.right(90)
        turtle.forward(side * 0.5)
        turtle.left(90)
        turtle.pendown()
#
#
def spider(length, number_of_legs):
    """draw square
    side = first size of the edge"""
    for a in range(1, number_of_legs + 1):
        angle_ = 360 // number_of_legs
        turtle.forward(length)
        turtle.left(180)
        turtle.forward(length)
        turtle.left(180 + angle_)


def spiral_():
    """draw square
    side = first size of the edge"""
    a = 0
    while a < 2:
        a += 0.001
        turtle.forward(a)
        turtle.left(1)

def square_spiral(first_side):
    """draw square spiral
    first_side = size of the first edge"""
    a = 1
    for a in range(20):
        for i in range(2):
            turtle.left(90)
            turtle.forward(first_side * a)
        a += 1

square_in_square(20, 3)
turtle.goto(0, 0)
turtle.clear()


spider(50, 10)
turtle.goto(0, 0)
turtle.clear()

window = turtle.Screen()
square_spiral(10)
window.exitonclick()

spiral_()
turtle.goto(0, 0)
turtle.clear()




