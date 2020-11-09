#Bron: https://pythonprogramming.net/threading-tutorial-python/?completed=/tkinter-adding-text-images/

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import serial as sr
import time

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Central panel")
        self.pack(fill="both",  expand=1)

        #maken van de button
        zonneScherm = Button(self, text="Zonnescherm", command=self.open_Zonnnescherm)
        lichtScherm = Button(self, text="Lichtscherm")

        #menubar
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Save", command=self.client_exit)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        #plaatsing van de buttons
        zonneScherm.place(x= 0, y=0)
        lichtScherm.place(x= 1, y=30)


    def client_exit(self):
        exit()
    
    #het openen van window zonnescherm
    def open_Zonnnescherm(self):
        top = Toplevel()
        top.title ('Zonnescherm central panel')
    
    #Openen van lichtsensorscherm
    def open_Lichtsensor(self):
        top = Toplevel()
        top.title ('lichtsensor central panel')
   

root = Tk()
root.geometry("50x90")
root.configure(background = 'light blue')

app = Window(root)
root.mainloop()