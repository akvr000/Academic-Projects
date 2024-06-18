# import tkinter
from tkinter import *
# from functools import partial

parent = Tk()
parent.geometry("400x300")
# parent.configure(background='steel blue')
c = Canvas(parent, bg="steel blue", width=1024, height=768)
c.pack()
# creating an arc
arc = c.create_arc((13, 17, 300, 300), start=0, extent=350, fill="yellow")
arc1 = c.create_arc((13, 17, 300, 300), start=0, extent=330, fill="green")
arc2 = c.create_arc((13, 17, 300, 300), start=0, extent=310, fill="purple")
arc3 = c.create_arc((13, 17, 300, 300), start=0, extent=280, fill="red")


parent.mainloop()
