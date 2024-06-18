"""from tkinter import *

top = Tk()
sb = Scrollbar(top)
sb.pack(side=RIGHT, fill=Y)

mylist = Listbox(top, yscrollcommand=sb.set)

for line in range(30):
    mylist.insert(END, "Number " + str(line))

mylist.pack(side=LEFT)
sb.config(command=mylist.yview)

top.mainloop()"""

"""from tkinter import *

top = Tk()
text = Text(top)
# text.insert(INSERT, "Name.....")
# text.insert(END, "Salary.....")
text.pack()

# text.tag_add("Write Here", "1.0", "1.4")
# text.tag_add("Click Here", "1.8", "1.13")

# text.tag_config("Write Here", background="yellow", foreground="black")
# text.tag_config("Click Here", background="black", foreground="white")

top.mainloop()"""

from tkinter import *

root = Tk()

root.geometry("200x200")


def open():
    top = Toplevel(root)
    
    top.mainloop()


btn = Button(root, text="open", command=open)

btn.place(x=75, y=50)

root.mainloop()
