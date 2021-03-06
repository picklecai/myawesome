#!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import time
import subprocess


class MyForm(BoxLayout):
    global switch
    switch = 1

    def start(self):
        global stime, dtime
        stime = time.time()
        dtime = self.ids['time_slider'].value
        self.ids['bg_image'].source = 'giphy.gif'
        Clock.schedule_interval(self.callback, 0.1)

    def callback(self, *argv):
        global stime, dtime
        if stime + dtime < time.time():
            self.ids['time_slider'].value = 0
            self.ids['time_counter'].text = '00:00.00'
            self.ids['bg_image'].source = 'giphy.png'
            subprocess.Popen(['open', 'alarm.wav'])
            return False
        self.ids['time_slider'].value = dtime + stime - time.time()

    def pause(self, *argv):
        global switch
        switch = switch * (-1)
        if switch == -1:
            Clock.unschedule(self.callback)
            self.ids['bg_image'].source = 'giphy.png'
        else:
            Clock.schedule_interval(self.callback, 0.1)
            self.ids['bg_image'].source = 'giphy.gif'

    def stop(self):
        self.ids['time_slider'].value = 0
        self.ids['time_counter'].text = '00:00.00'
        self.ids['bg_image'].source = 'giphy.png'
        Clock.unschedule(self.callback)


class ClockApp(App):

    def build(self):
        Window.fullscreen = 1
        Window.size = (320, 640)
        self.title = 'Countdown Clock -PICKLECAI'
        return MyForm()

if __name__ == '__main__':
    ClockApp().run()
