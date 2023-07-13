# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 23:15:10 2023

@author: neera

"""

import tkinter as tk
from PIL import Image, ImageTk
from imutils.video import VideoStream
import cv2
import datetime

class MainWindow:

    def __init__(self):    
        self.window = tk.Tk()
        
        self.panel = tk.Label(self.window)
        self.panel.pack(side="top")
        
        self.button = tk.Button(self.window, text='Take Photos', command=self.take_photo)
        self.button.pack(side="bottom")
        
        self.stream = VideoStream(0)
        self.stream.start()
        
        self.stop = False
        self.window.after(100, self.video_loop)

        self.window.wm_protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.mainloop()

    def video_loop(self):
        frame = self.stream.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.image = Image.fromarray(image)
        self.photo = ImageTk.PhotoImage(self.image)
        self.panel.configure(image=self.photo)  
        if not self.stop:
            self.window.after(40, self.video_loop)

    def on_close(self):
        self.stop = True
        self.stream.stop()
        self.window.destroy()
    def take_photo(self):
        name = datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S.png')
        self.image.save(name, 'PNG')
        print('saved:', name)
           
if __name__ == '__main__':
    MainWindow()