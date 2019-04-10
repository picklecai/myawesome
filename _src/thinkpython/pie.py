# _*_ coding: utf-8 _*_

from swampy.TurtleWorld import *
from math import pi, sin

world = TurtleWorld()

bob = Turtle()
'''
bob.delay = 0.0001
ray = Turtle()
ray.delay = 0.0001
'''


'''
def polygon(t, length, n):
    if n == 0:
        return
    angle = 360.0 / n
    fd(t, length)
    rt(t, angle) # 右转非90度。
    polygon(t, length, n - 1)

# angle必须不变，所以这里不能用递归。

'''


def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        rt(t, 360.0 / n)  # 右转非90度。


def polyline(t, length, n):
    for i in range(n):
        fd(t, length)
        pu(t)
        bk(t, length)
        pd(t)
        rt(t, 360.0 / n)

n = input("Please input a number:")

length = 80.0
r = length / (2 * sin(1.0 / n * pi))
print length, r, sin(1.0 / n * pi)

polyline(bob, r, n)
lt(bob, 360.0 / n)
pu(bob)
fd(bob, r)
pd(bob)
rt(bob, 90 + 180.0 / n)
polygon(bob, length, n)


wait_for_user()
