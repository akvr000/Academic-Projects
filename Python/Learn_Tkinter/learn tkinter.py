# import web-browser
from tkinter import *
# import webview
from tkinter import messagebox

root = Tk()

root.geometry("400x400")

"""def open():
    web-browser.open("https://www.codewithharry.com/videos/python-gui-tkinter-hindi-1/")

    Button(root, text="click me", command=open).pack()"""

"""label = LabelFrame(root, text="hi there", height=600)
label.pack(fill=BOTH)
label1 = Label(label, text="hello everyone ")
label1.pack()"""
labelframe = LabelFrame(root, text="hi there")
labelframe.pack(fill=X)
label2 = Label(labelframe, text="hello everyone ")
label2.pack()


# learn tkinter messagebox
def message_box():
    messagebox.showinfo(title="hello", message="this window is created by Anjali!")
    messagebox.showwarning(title="Alert", message="This site can be harmful for your device!")
    messagebox.askquestion(title="warning", message="Do you still want to continue?")
    messagebox.askyesno(title="warning", message="yes or no?")
    messagebox.askyesno(title="Installation", message="Do you want to install it?")
    messagebox.showerror(title="Error", message="Please try again later!")
    messagebox.askretrycancel(title="Installation", message="Try again later!")
    messagebox.askokcancel(title="Installation", message="Couldn't be installed!")
    messagebox.showerror(title="Error", message="Please try again later!")


button = Button(root, text="Click Here!", command=message_box)
button.pack()

root.mainloop()
