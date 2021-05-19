import turtle as t
import math
from typing import List


def num(n):
    """ draw numbers that come from arg n """
    if n == 1:
        t.penup()
        t.goto(0, -40)
        t.pendown()
        t.left(45)
        t.forward(math.sqrt(40 ** 2 + 40 ** 2))
        t.right(180 - 45)
        t.forward(80)
    if n == 2:
        t.forward(40)
        t.right(90)
        t.forward(40)
        t.right(45)
        t.forward(math.sqrt(40 ** 2 + 40 ** 2))
        t.left(180 - 45)
        t.forward(40)
    if n == 3:
        for _ in range(3):
            t.forward(40)
            t.right(90)
        t.right(90)
        for _ in range(3):
            t.forward(40)
            t.right(90)
    if n == 4:
        t.right(90)
        for _ in range(3):
            t.forward(40)
            t.left(90)
        t.left(90)
        t.forward(80)
    if n == 5:
        t.forward(40)
        t.right(180)
        t.forward(40)
        t.left(90)
        t.forward(40)
        t.left(90)
        t.forward(40)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(40)
    if n == 6:
        t.forward(40)
        t.right(180)
        t.forward(40)
        t.left(90)
        t.forward(80)
        for _ in range(3):
            t.left(90)
            t.forward(40)
    if n == 7:
        t.forward(40)
        t.right(135)
        t.forward(math.sqrt(40 ** 2 + 40 ** 2))
        t.left(45)
        t.forward(40)
    if n == 8:
        t.forward(40)
        t.right(180)
        t.forward(40)
        t.left(90)
        t.forward(80)
        for _ in range(3):
            t.left(90)
            t.forward(40)
        t.backward(40)
        t.right(90)
        t.forward(40)
    if n == 9:
        for _ in range(3):
            t.forward(40)
            t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(40)
    if n == 0:
        t.forward(40)
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(80)


tex = open('teeee.txt', 'r')


a: List[str] = tex.readline().split()
i: int
window = t.Screen()
for i in range(len(a)):
    a[i] = int(a[i])
    t.penup()
    t.home()
    t.goto(60 * i, 0)
    t.pendown()
    num(a[i])
window.exitonclick()
tex.close()
