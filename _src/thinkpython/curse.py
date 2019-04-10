# _*_ coding: utf-8 _*_

from swampy.TurtleWorld import *
from math import pi, cos

world = TurtleWorld()

bob = Turtle()
bob.delay = 0.0001


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length * n)
    lt(t, angle)
    draw(t, length, n - 1)
    rt(t, 2 * angle)
    draw(t, length, n - 1)
    lt(t, angle)
    bk(t, length * n)


def koch1(t, length, n):
    if length < n:
        fd(t, length)
        return  # 如果不加，程序就会死循环，啥也干不了。
    for i in range(n):
        if i % 2 == 0:
            koch1(t, length / n, n)
            lt(t, 180.0 / n)
        else:
            koch1(t, length / n, n)
            rt(t, 360.0 / n)
    koch1(t, length / n, n)


def koch2(t, length, n):
    if length < n:
        fd(t, length)
        return  # 如果不加，程序就会死循环，啥也干不了。
    koch2(t, length / n, n)
    lt(t, 180.0 / n)
    koch2(t, length / n, n)
    rt(t, 360.0 / n)
    koch2(t, length / n, n)
    lt(t, 180.0 / n)
    koch2(t, length / n, n)


def koch0(t, length):
    if length < 3:
        fd(t, length)
        return
    koch0(t, length / 3.0)
    lt(t, 60)
    koch0(t, length / 3.0)
    rt(t, 120)
    koch0(t, length / 3.0)
    lt(t, 60)
    koch0(t, length / 3.0)


def snowflake(t, length, n):
    for i in range(n):
        koch1(bob, length, n)
        rt(bob, 360.0 / n)


def archispiral(t, length, alpha, n):
    c = (length ** 2 + (length * (n + 1)) ** 2 - 2 * length ** 2 * (n + 1) * cos(alpha / 180 * pi)) ** 0.5
    fd(t, c)
    rt(t, alpha)
    if n < 1:
        pu(t)
        fd(t, length)
        return
    archispiral(t, length, alpha, n - 1)


# 乌龟的位置向下移动一些。
rt(bob, 90)
pu(bob)
fd(bob, 80)
lt(bob, 90)
pd(bob)


# draw(bob, 15, 5)

length = input("Input a float numeber:")
n = input("Input a number:")
alpha = 5

'''koch1(bob, length, n)

pu(bob)
fd(bob, 200)
pd(bob)
koch2(bob, length, n)

pu(bob)
fd(bob, 200)
pd(bob)
koch0(bob, length)

pu(bob)
fd(bob, 200)
pd(bob)


snowflake(bob, length, n)
'''
archispiral(bob, length, alpha, n)

pu(bob)
fd(bob, 200)
pd(bob)

wait_for_user()
