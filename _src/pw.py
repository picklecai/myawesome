# python3
# pw.py
# __coding:utf-8__
# This is a keyword box

import sys
import pyperclip

'''
PASSWORD = {"email": "eTfGIM2BZbYH7fxS", "blog": "a7QEHvM6Rszzo9Uj",
            "luggage": "12345"}  # control + alt + R
'''

desk_path = '/Users/caimeijuan/github/myawesome/_src/'
full_path = desk_path + 'pw' + '.txt'
passwordFile = open(full_path)
lines = passwordFile.readlines()  # Not read 2 times, or the 2nd will tell: list index out of range.

keywords = (lines[0].strip("\n")).split(" ")
passwords = lines[1].split(" ")
PASSWORD = dict(zip(keywords, passwords))

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]


'''
print(PASSWORD.get(account, "This account isn\'t exist."))
pyperclip.copy(PASSWORD.get(account, "This account isn\'t exist."))
print(pyperclip.paste())
'''

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print("Password for " + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
