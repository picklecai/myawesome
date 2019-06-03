#!/usr/bin/env python
# _*_coding:utf-8_*_

import pyautogui
import time


def filler():
    nameField = (183, 294)
    # submitButton = (562, 636)
    # submitButtonColor = (0, 104, 239)
    submitAnotherLink = (205, 272)

    formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
                 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
                {'name': 'Bob', 'fear': 'bees', 'source': 'amulet',
                 'robocop': 4, 'comments': 'n/a'},
                {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
                 'robocop': 1,
                 'comments': 'Please take the puppets out of the break room.'},
                {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
                 'robocop': 5, 'comments': 'Protect the innocent. Serve the \
                 public trust. Upload the law.'}, ]
    for person in formData:
        print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
        time.sleep(5)

        time.sleep(0.5)
        print('Entering %s info...' % (person['name']))
        pyautogui.click(nameField[0], nameField[1])
        pyautogui.typewrite(person['name'] + '\t')
        pyautogui.typewrite(person['fear'] + '\t')

        if person['source'] == 'wand':
            pyautogui.typewrite(['enter', 'down', 'enter', '\t'], 0.25)
        elif person['source'] == 'amulet':
            pyautogui.typewrite(['enter', 'down', 'down', 'enter', '\t'], 0.25)
        elif person['source'] == 'crystal ball':
            pyautogui.typewrite(['enter', 'down', 'down', 'down', 'enter', '\t'], 0.25)
        elif person['source'] == 'money':
            pyautogui.typewrite(['enter', 'down', 'down', 'down', 'down', 'enter', '\t'], 0.25)

        if person['robocop'] == 1:
            pyautogui.typewrite([' ', '\t'])
        elif person['robocop'] == 2:
            pyautogui.typewrite(['right', '\t'])
        elif person['robocop'] == 3:
            pyautogui.typewrite(['right', 'right', '\t'])
        elif person['robocop'] == 4:
            pyautogui.typewrite(['right', 'right', 'right', '\t'])
        elif person['robocop'] == 5:
            pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

        pyautogui.typewrite(person['comments'] + '\t', 0.25)
        pyautogui.press('enter')

        print('Clicked Submit.')
        time.sleep(5)

        pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])


def main():
    filler()


if __name__ == '__main__':
    main()
