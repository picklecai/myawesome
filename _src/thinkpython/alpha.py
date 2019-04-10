# _*_ coding: utf-8 _*_

from swampy.TurtleWorld import *
# from math import pi, sin

world = TurtleWorld()

bob = Turtle()


def draw_a(t, font_n):
    # 调整初始方向
    rt(t, 120.0)
    # 开始画
    fd(t, font_n)
    pu(t)
    bk(t, font_n)
    pd(t)
    lt(t, 60.0)
    fd(t, font_n)
    pu(t)
    bk(t, font_n)
    rt(t, 60.0)
    fd(t, font_n * (2.0 / 3))
    pd(t)
    lt(t, 120.0)
    fd(t, font_n * (2.0 / 3))
    # 笔触到下一个位置准备
    pu(t)
    fd(t, font_n)
    lt(t, 90.0)
    fd(t, font_n * (2.0 / 3))
    rt(t, 180.0)
    pd(t)


def draw_b(t, font_n):



draw_a(bob, 80)


wait_for_user()