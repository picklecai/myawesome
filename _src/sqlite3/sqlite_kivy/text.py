#!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
from os.path import exists
import os
import time
import sqlite3


class MyForm(BoxLayout):
    text_input = ObjectProperty()
    label_text = StringProperty()
    global ROOT
    ROOT = os.getcwd()

    def print_history(self):
        if exists('abcrecord.db'):
            with sqlite3.connect(ROOT + '/abcrecord.db') as conn:
                cur = conn.cursor()
                cur.execute('create table if not exists record (time text, record text)')
                cur.execute('select * from record')
                notelist = cur.fetchall()
                cur.close()
                conn.commit()
            self.label_text = str(notelist)
        else:
            self.label_text = '程序第一次运行，还没有历史记录。请录入新内容。'

    def save(self):
        newline = self.text_input.text
        nowtime = time.strftime('%Y/%m/%d %H:%M:%S')
        data = (nowtime, newline)
        with sqlite3.connect(ROOT + '/abcrecord.db') as conn:
            cur = conn.cursor()
            cur.execute('create table if not exists record (time text, record text)')
            cur.execute('insert into record (time, record) values (?, ?)', data)
            cur.close()
            conn.commit()

    def clear(self):
        self.label_text = ''


class TextApp(App):

    def build(self):
        Window.fullscreen = 1
        Window.size = (320, 640)
        self.title = 'NOTEBOOK-PICKLECAI'
        return MyForm()

if __name__ == '__main__':
    TextApp().run()
