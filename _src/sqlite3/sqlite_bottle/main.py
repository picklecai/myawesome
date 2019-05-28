#!/usr/bin/env python
# _*_coding:utf-8_*_
import sqlite3
import os
import time
from bottle import run, route, post, template, request


@route('/')
def index():
    return template('index', savetxt=False)


@post('/', method='POST')
def save():
    newline = request.forms.decode('utf-8').get('record')
    nowtime = time.strftime('%Y/%m/%d %H:%M:%S')
    data = (nowtime, newline)
    with sqlite3.connect(ROOT + '/abcrecord.db') as conn:
        cur = conn.cursor()
        cur.execute('create table if not exists record (time text, record text)')
        cur.execute('insert into record (time, record) values (?, ?)', data)
        cur.close()
        conn.commit()
    return template('index', savetxt=True)


@route('/history')
def print_history():
    if os.path.exists('abcrecord.db'):
        with sqlite3.connect(ROOT + '/abcrecord.db') as conn:
            cur = conn.cursor()
            cur.execute('create table if not exists record (time text, record text)')
            cur.execute('select * from record')
            notelist = cur.fetchall()
            cur.close()
            conn.commit()
    else:
        notelist = []
    return template('history', history=notelist)


'''
def inputnew():
    newline = input('Please input')
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
        return notelist
'''
if __name__ == '__main__':
    global HOST, PORT, ROOT
    HOST = '127.0.0.1'
    PORT = 65432
    ROOT = os.getcwd()
    run(host=HOST, port=PORT, debug=True, reloader=True)
