#!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.core.window import Window


class MyForm(BoxLayout):
    label_text = StringProperty()
    global num
    num = 10

    def countback(self):
        global num
        self.update()

    def update(self):
        Clock.schedule_once(self.callback, 1)

    def callback(self, *argv):
        global num
        self.label_text = str(num)
        num = num - 1
        self.update()
        if num < 0:
            print('Byebye.')
            Clock.unschedule(self.callback)
            return False


class CountbackApp(App):

    def build(self):
        Window.fullscreen = 1
        Window.size = (320, 320)
        self.title = 'Count Back - PICKLECAI'
        return MyForm()

if __name__ == '__main__':
    CountbackApp().run()
