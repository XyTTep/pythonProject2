import turtle
import math

turtle.shape('arrow')


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
    turtle.resetscreen()


def spider(length, number_of_legs):
    """draw spider
    side = first size of the edge"""
    for a in range(1, number_of_legs + 1):
        angle_ = 360 // number_of_legs
        turtle.forward(length)
        turtle.left(180)
        turtle.forward(length)
        turtle.left(180 + angle_)
    turtle.resetscreen()


def spiral_():
    """draw spiral
    side = first size of the edge"""
    a = 0
    while a < 2:
        a += 0.001
        turtle.forward(a)
        turtle.left(1)
    turtle.resetscreen()


def square_spiral(first_side):
    """draw square spiral
    first_side = size of the first edge"""
    for i in range(20):
        for j in range(2):
            turtle.left(90)
            turtle.forward(first_side * i)
    turtle.resetscreen()


def polygon(n, radius_1):
    """ draw polygonal figures
    n - number of angles
    radius_1 - radius of the circumscribed circle of the triangle """
    for i in range(3, n + 1):
        a = radius_1 * (2 * math.sin((180 / i) * (math.pi / 180)))
        turtle.left(180 * (i - 2) / (2 * i))
        for _ in range(i):
            turtle.left(180 - (180 * (i - 2) / i))
            turtle.forward(a)
        radius_1 += 20
        turtle.penup()
        turtle.right(180 * (i - 2) / (2 * i))
        turtle.forward(20)
        turtle.pendown()


def flower(radius, n):
    for i in range(n):
        turtle.circle(radius, 360, 10)
        turtle.circle(-radius, 360, 10)
        turtle.right(360 / n)


def super_8(rad_1, n):
    turtle.left(90)
    for i in range(n):
        turtle.circle(rad_1, 360, 10)
        turtle.circle(-rad_1, 360, 10)
        rad_1 += 10


def spiral(rad_1, n):
    turtle.right(-90)
    for i in range(n):
        turtle.circle(-rad_1, 180, 10)
        turtle.circle(-rad_1 / 4, 180, 10)


def smile(first_point_x, first_point_y, size):
    """first_point - center of the smile
    size - radius of the smile"""
    turtle.fillcolor("light yellow")
    turtle.penup()
    turtle.goto(first_point_x, first_point_y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size / 2, 360, 20)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0.57 * (size / 2) + first_point_x, first_point_x + (size / 2) + (size / 2) * 0.2)
    turtle.pendown()
    turtle.fillcolor("light green")
    turtle.begin_fill()
    turtle.circle((size / 2) * 0.2, 360, 20)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(first_point_x - 0.57 * (size / 2), first_point_x + (size / 2) + (size / 2) * 0.2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle((size / 2) * 0.2, 360, 20)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(first_point_x, first_point_y + (size / 2))
    turtle.width(5)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(0.2 * (size / 2))
    turtle.penup()
    turtle.goto(first_point_x - 0.57 * (size / 2), first_point_x + (size / 2) + (size / 2) * 0.2)  # right eye
    turtle.forward((size / 3.7))
    turtle.pendown()
    turtle.pencolor("pink")
    turtle.circle(size / 3.5, 180)
    turtle.pendown()


window = turtle.Screen()

smile(10, 10, 200)
turtle.reset()
polygon(5, 20)
turtle.reset()
flower(50, 10)
turtle.reset()
super_8(50, 5)
turtle.reset()
spiral(50, 5)
turtle.reset()
square_in_square(20, 3)
turtle.reset()
spider(50, 10)
turtle.reset()
square_spiral(10)
turtle.reset()
spiral_()
turtle.reset()

window.exitonclick()
