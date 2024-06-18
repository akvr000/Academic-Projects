# from tkinter import Tk, Menu, Toplevel
from tkinter import filedialog
from tkinter import *
from tkinter import Scrollbar

top = Tk()
menubar = Menu(top)
top.geometry("500x500")
top.title("Untitled - Notepad")
top.iconbitmap("D:\downloads from chrome\logo.ico")
top.config(menu=menubar)

# creating scrollbar

sb = Scrollbar(top)
sb.pack(side=RIGHT, fill=Y)

textarea = Text(top, yscrollcommand=sb.set, height=756, width=1024)
textarea.pack()
sb.config(command=textarea.yview)

# creating text area
# text = Text(top, height=756, width=1024)
# text.pack()


def font():
    sip = Toplevel(top)
    sip.geometry("400x500")
    sip.title("Font...")
    sip.iconbitmap("D:\downloads from chrome\logo.ico")
    fo = StringVar()
    fon = Label(sip)
    fo_t = Label(sip, text="Font:")
    fo_t.grid(row=3, column=1)
    font_t = Entry(top)
    font_t.grid(row=4, column=1)
    sip.mainloop()


def open():
    global open
    open = filedialog.askopenfile()


def save():
    global save
    global saves
    saves = [('All Files', '.'),
             ('Paython Files', '.py'),
             ('Word Files', '.docx'),
             ('Image Files', '.jpg, .png')]
    save = filedialog.asksaveasfile(filetypes=saves, defaultextension=save)


def save_as():
    global save_A
    save_A = filedialog.asksaveasfilename()


def exit():
    top.destroy()
    # top.quit()


menubar = Menu(top)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="New Window")
file.add_command(label="Open...", command=open)
file.add_command(label="Save", command=save)
file.add_command(label="Save as...", command=save_as)
file.add_separator()
file.add_command(label="Page Setup...")
file.add_command(label="Print...")
file.add_separator()
file.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=file)

edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_separator()
edit.add_command(label="Search With Bing...")
edit.add_command(label="Find...")
edit.add_command(label="Find Next")
edit.add_command(label="Find Previous")
edit.add_command(label="Replace...")
edit.add_command(label="Go To...")

edit.add_separator()
edit.add_command(label="Select All")
edit.add_command(label="Time/Date")
menubar.add_cascade(label="Edit", menu=edit)

Format = Menu(menubar, tearoff=0)
Format.add_checkbutton(label="Word Wrap")
Format.add_command(label="Font...", command=font)
menubar.add_cascade(label="Format", menu=Format)

view = Menu(menubar, tearoff=0)
view.add_cascade(label="Zoom")
view.add_checkbutton(label="Status Bar")
menubar.add_cascade(label="View", menu=view)

help = Menu(menubar, tearoff=0)
help.add_command(label="View Help")
help.add_command(label="Send Feedback")
help.add_separator()
help.add_command(label="About Notepad")
menubar.add_cascade(label="Help", menu=help)

top.config(menu=menubar)
top.mainloop()
