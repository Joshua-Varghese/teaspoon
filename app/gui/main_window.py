from tkinter import *
import pandas as pd
import numpy as np


root = Tk()
root.title('teaspoon')
root.geometry('500x500')

option_frame = Frame(root)
option_frame.pack()

info_frame = Frame(root)
info_frame.pack()

loadbtn = Button(option_frame,text="Load Dataset")
loadbtn.pack()

edabtn = Button(option_frame,text="EDA Analysis")
edabtn.pack()

root.mainloop()
