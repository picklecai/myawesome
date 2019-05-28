#!/usr/bin/env python
# _*_coding:utf-8_*_
import sqlite3
import os
import time


def inputnew():
    newline = input('Please input: ')
    nowtime = time.strftime('%Y/%m/%d %H:%M:%S')
    data = (nowtime, newline)
    with sqlite3.connect(ROOT + '/abcrecord.db') as conn:
        cur = conn.cursor()
        cur.execute('create table if not exists record (time text, record text)')
        cur.execute('insert into record (time, record) values (?, ?)', data)
        cur.close()
        conn.commit()


def print_history():
    with sqlite3.connect(ROOT + '/abcrecord.db') as conn:
        cur = conn.cursor()
        cur.execute('create table if not exists record (time text, record text)')
        cur.execute('select * from record')
        notelist = cur.fetchall()
        cur.close()
        conn.commit()
        print(notelist)

if __name__ == '__main__':
    global ROOT
    ROOT = os.getcwd()
    inputnew()
    print_history()
