#Bron: https://pythonprogramming.net/


import tkinter as tk           
from tkinter import font as tkfont  
import serial
import csv
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation 
from matplotlib import style


style.use("ggplot")

#maakt plot voor graph
f = Figure(figsize=(8,5), dpi=100)
a = f.add_subplot(211)


def animate(i):
    plt.ion()

    i=0
    x=list()
    y=list()

    ser = serial.Serial('COM4', 19200)

    ser.close()
    ser.open()

    while True:
        data = ser.readline()
        print(data.decode())
        x.append(i)
        y.append(data.decode())

        plt.scatter(i, str(data.decode()))

        i += 1
        plt.show
        plt.pause(0.0001)


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Zonnesensor, Lichtsensor):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
    
        


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Central panel", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Zonnesensor panel",
                            command=lambda: controller.show_frame("Zonnesensor"))
        button2 = tk.Button(self, text="Licht sensor panel",
                            command=lambda: controller.show_frame("Lichtsensor"))
        button1.pack()
        button2.pack()

class Zonnesensor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Temperatuur control panel", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10, padx=10)

        button = tk.Button(self, text="Homepage",   
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


        # plaats grafiek het in de page zonnesensor
        Fig1 = FigureCanvasTkAgg(f, self)
        Fig1.draw()
        Fig1.get_tk_widget().pack(side=tk.TOP, fill= tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(Fig1, self)
        toolbar.update()
        Fig1._tkcanvas.pack(side=tk.TOP, fill= tk.BOTH, expand=True)
    


class Lichtsensor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Licht control panel", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10, padx=10)
        button = tk.Button(self, text="Homepage",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        scl = tk.Scale(self,orient="horizontal", resolution=1, from_=0, to=120)
        scl.pack() 
        button2 = tk.Button(self, 
                            bg="red", fg="black" 
                            ,text="Zonnescherm omhoog (cm)")
        button2.pack()

        # plaats het in de page zonnesensor
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill= tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill= tk.BOTH, expand=True)



if __name__ == "__main__":
    app = MainApp()
    ani = animation.FuncAnimation(f, animate, interval=1000)
    app.mainloop()