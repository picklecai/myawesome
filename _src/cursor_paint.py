#!/usr/bin/env python
# _*_coding:utf-8_*_

import pyautogui
import time


def cursor():
    time.sleep(5)
    pyautogui.click()
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)
        pyautogui.dragRel(-distance, 0, duration=0.2)
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.2)


def main():
    cursor()

if __name__ == '__main__':
    main()
