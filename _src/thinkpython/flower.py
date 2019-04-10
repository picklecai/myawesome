# _*_ coding: utf-8 _*_

from swampy.TurtleWorld import *
from math import pi

world = TurtleWorld()

bob = Turtle()
bob.delay = 0.0001
ray = Turtle()
ray.delay = 0.0001


def polyline(t, angle, length, n):
    for i in range(n):
        fd(t, length)
        rt(t, angle / n)


def arc(t, r, angle):
    arc_circum = 2 * pi * r * angle / 360.0
    n = int(arc_circum / 10)
    length = arc_circum / n
    polyline(t, angle, length, n)


def draw_flower1(n):
    for i in range(n):
        arc(bob, 50, 360.0 / n * 2)
        lt(bob, 360.0 / n)


def draw_flower2(n):
    for i in range(n):
        arc(bob, 50, 360.0 / n * 2)
        rt(bob, 360.0 / n)


def draw_flower3(n):
    for i in range(n):
        arc(bob, 50, 360.0 / n * 2)
        rt(bob, 180 - 360.0 / n * 2)
        arc(bob, 50, 360.0 / n * 2)
        rt(bob, 180 - 360.0 / n)


def draw_flower4(n):
    for i in range(n):
        arc(bob, 50, 360.0 / n)
        rt(bob, 180 - 360.0 / n * 2)
        arc(bob, 50, 360.0 / n)
        rt(bob, 180 - 360.0 / n)


n = input('Input the number:')
for i in range(5):
    if n % 2 == 0:
        draw_flower3(n)
    elif n % 2 != 0:
        draw_flower4(n)
    pu(bob)
    fd(bob, 200)
    pd(bob)
    n = n + 1


wait_for_user()
