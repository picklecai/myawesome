#!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.clock import Clock
import time


class MyForm(BoxLayout):
    text_input = ObjectProperty()
    label_text1 = StringProperty()  # 这是个文本属性
    global num
    num = 10

    def buttona_act(self):
        print(self.text_input.text)
        self.label_text1 = self.text_input.text

    def buttonb_act(self):
        global stime, dtime
        stime = time.time()
        dtime = self.ids['time_slider'].value
        self.on_update()

    def callback(self, *argv):
        global stime, dtime
        if stime + dtime < time.time():
            self.ids['time_slider'].value = 0
            self.ids['time_counter'].text = '00:00:00'
            Clock.unschedule(self.callback)
            return False
        self.ids['time_slider'].value = dtime + stime - time.time()
        self.on_update()

    def on_update(self):
        Clock.schedule_once(self.callback, 0.2)

    def my_callback(self, *argv):
        global num
        # print('my callback is called', num)
        self.label_text1 = str(num)
        num = num - 1
        if num == 0:
            print('Byebye.')
            return False
        self.update()

    def update(self):
        Clock.schedule_interval(self.my_callback, 1)


class NoteApp(App):
    pass

if __name__ == '__main__':
    NoteApp().run()
