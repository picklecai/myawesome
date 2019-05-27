# _*_ coding:utf-8 _*_

import os
from os.path import join, getsize


def getdirsize(dir):
    size = 0.0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size

if __name__ == '__main__':
    dir = os.getcwd()
    filesize = getdirsize(dir)
    print('There are %.2f' % (filesize / 1024 / 1024), 'Mbytes here.')
