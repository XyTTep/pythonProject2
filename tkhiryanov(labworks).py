import turtle

window = turtle.Screen()
turtle.shape('turtle')


def square(side, number_of_squares):
    """draw rectangle
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


square(20, 5)
window.exitonclick()