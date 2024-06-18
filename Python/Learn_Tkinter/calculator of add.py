from tkinter import *


# from PIL import Image, ImageTk

def add():
    a = int(e1.get())
    b = int(e2.get())

    leftdata = str(a + b)
    left.insert(1, leftdata)


root = Tk()
root.geometry("400x300+200+100")
root.minsize(350, 290)
# root.maxsize(300, 400)
text = Label(root, text="Here is your Calculator!", font="Helvetica, 20", pady=15)
text.pack()

w1 = PanedWindow(root, bg="red", border=3, height=170)
w1.pack()

left = Entry(w1, font="helvetica,80", background="yellow")
w1.add(left)

w2 = PanedWindow(w1, orient=VERTICAL, bg="red", background="green")
w1.add(w2)

e1 = Entry(w2, font="helvetica,80", background="yellow")
e2 = Entry(w2, font="helvetica,80", background="yellow")

w2.add(e1)
w2.add(e2)

photo = PhotoImage(file="D:\Anjali Kumari\python codes\images\images (12).png", height=160, width=327)
label = Button(w2, image=photo, command=add, height=130, width=300)
w2.add(label)

root.mainloop()
