import turtle

# window = turtle.Screen()
turtle.shape('turtle')


# def square(side, number_of_squares):
#     """draw square
#     side = first size of the edge"""
#     for a in range(1, number_of_squares + 1):
#         for i in range(4):
#             turtle.left(90)
#             turtle.forward(side * a)
#         turtle.penup()
#         turtle.forward(side * 0.5)
#         turtle.right(90)
#         turtle.forward(side * 0.5)
#         turtle.left(90)
#         turtle.pendown()
#
#
# def spider(length, number_of_legs):
#     """draw square
#     side = first size of the edge"""
#     for a in range(1, number_of_legs + 1):
#         angle_ = 360 // number_of_legs
#         turtle.forward(length)
#         turtle.left(180)
#         turtle.forward(length)
#         turtle.left(180 + angle_)


def spiral_():
    """draw square
    side = first size of the edge"""
    a = 0
    while a < 2:
        a += 0.001
        turtle.forward(a)
        turtle.left(1)



# square(20, 3)
# turtle.clear()

window = turtle.Screen()
spiral_()
window.exitonclick()
