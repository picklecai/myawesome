#!/usr/bin/env python
# _*_coding:utf-8_*_

import pyautogui


def cursor():
    print('Press Ctrl - C to quit.')
    try:
        while True:
            # print(pyautogui.position())
            x, y = pyautogui.position()
            positionStr = ('  X: %s Y: %s') % (str(x).rjust(4), str(y).rjust(4))
            pixelColor = pyautogui.screenshot().getpixel((x, y))
            positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
            positionStr += ', ' + str(pixelColor[1]).rjust(3)
            positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
            print(positionStr, end='')  # 这一行忘记写end=‘’
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\nDone.')


def main():
    cursor()

if __name__ == '__main__':
    main()
