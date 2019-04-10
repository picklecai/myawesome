# _*_ coding: utf-8 _*_


def mylife(x):
    if x > 0:
        return x
    elif x < 0:
        return -x


def right_justify(s):
    print(' ' * (70 - len(s)) + s)


def do_four(f, n):
    for i in [1, 2, 3, 4]:
        f(n)


def print_twice(s):
    print(s)
    print(s)


def print_sqr(m, n):
    for i in [1, 2]:
        print('+' + '_' * n + '+' + '_' * n + '+')
        for j in range(m):
            print('|' + ' ' * n + '|' + ' ' * n + '|')
    print('+' + '_' * n + '+' + '_' * n + '+')

'''

name = raw_input('Please input your name:')
print('Hello', name)

x = input('Input a number:')
print(mylife(x))

right_justify('ahcai is hhhhhhhhhhhhhhh')

s = 'ahcai'
do_four(print_twice, s)

hight = input('Please input a hight number:')
wide = input('Please input a wide number:')
print_sqr(hight, wide)

'''

