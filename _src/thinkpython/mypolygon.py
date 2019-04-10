# _*_ coding: utf-8 _*_

from swampy.TurtleWorld import *
from math import pi

world = TurtleWorld()

bob = Turtle()
bob.delay = 0.0001
ray = Turtle()
ray.delay = 0.0001


'''
length = input('Please input length:')
square(bob, length)
polygon(bob, n / 3, n)
circle(bob, r)

r = input('Input the radio:')
angle = input('Input the angle:')
arc(bob, r, angle)

polygon(ray, 40, 4)

circle(bob, 50)
circle1(ray, 70)

'''


def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)


def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        rt(t, 360.0 / n)  # 右转非90度。


def circle(t, r):
    n = 60
    for i in range(n):
        fd(t, 2 * pi * r / n)
        lt(t, 360.0 / n)


def circle1(t, r):
    circum = 2 * pi * r
    n = int(circum / 10)
    length = circum / n
    polygon(t, length, n)


def arc_cuo(t, r, angle):
    n = 60
    for i in range(n):
        fd(t, 2 * pi * r / n)  # 周长除以n，这是错误的。
        lt(t, angle / n)


def arc(t, r, angle):
    arc_circum = 2 * pi * r * angle / 360
    n = int(arc_circum / 10)
    length = arc_circum / n
    for i in range(n):
        fd(t, length)
        lt(t, angle / n)


def polyline(t, angle, length, n):
    for i in range(n):
        fd(t, length)
        rt(t, angle / n)


def arc1(t, r, angle):
    arc_circum = 2 * pi * r * angle / 360
    n = int(arc_circum / 10)
    length = arc_circum / n
    polyline(t, angle, length, n)


def polygon1(t, length, n):
    polyline(t, 360.0 / n, length, n)

def circle2(t, r):
	arc1(t, r, 360)

circle(ray, 90)
circle1(bob, 90)

wait_for_user()

