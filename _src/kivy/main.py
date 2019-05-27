#!/usr/bin/env python
# _*_coding:utf-8_*_
import sqlite3
import os
import time


def main():
    global ROOT
    ROOT = os.path.dirname(os.getcwd())
    content = input('Please input:')
    nowtime = time.strftime('%Y/%m/%d %H:%M:%S')
    data = (nowtime, content)
    inputnew(data)


def inputnew(data):
    with sqlite3.connect(ROOT + '/noterecord.db') as conn:
        with conn.cursor() as cursor:
            cursor.execute('create table if not exists record (time text, record text)')
            cursor.execute('insert into record (time, record) values (?, ?)', data)
        conn.commit()

if __name__ == '__main__':
    main()
