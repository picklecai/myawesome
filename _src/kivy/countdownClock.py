#!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import time


class MyForm(BoxLayout):
    def start(self):
        global stime, dtime
        stime = time.time()
        dtime = self.ids['time_slider'].value
        self.on_update()

    def on_update(self):
        Clock.schedule_once(self.callback, 0.1)

    def callback(self, *argv):
        global stime, dtime
        if stime + dtime < time.time():
            self.ids['time_slider'].value = 0
            self.ids['time_counter'].text = '00:00.00'
            Clock.unschedule(self.callback)
            return False
        self.ids['time_slider'].value = dtime + stime - time.time()
        self.on_update()


class ClockApp(App):

    def build(self):
        Window.fullscreen = 1
        Window.size = (320, 640)
        self.title = 'Countdown Clock -PICKLECAI'
        return MyForm()

if __name__ == '__main__':
    ClockApp().run()
