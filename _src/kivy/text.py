#!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
from os.path import exists
import time


class MyForm(BoxLayout):
    text_input = ObjectProperty()
    label_text = StringProperty()

    def print_history(self):
        if exists('tempfile.txt'):
            with open('tempfile.txt') as f:
                txt = f.read()
            self.label_text = txt
        else:
            self.label_text = '程序第一次运行，还没有历史记录。请录入新内容。'

    def save(self):
        with open('tempfile.txt', 'a') as f:
            content = self.text_input.text
            if content != '':
                f.write(time.strftime('%Y/%m/%d %H:%M:%S' + '\n'))
                f.write(content + '\n' + '\n' + '=' * 27 + '\n' + '\n')
            else:
                return

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
