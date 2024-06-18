import os
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename

# made by Anjali

top = Tk()
top.geometry("500x400")
top.title("Untitled - Notepad")
#top.iconbitmap(r"D:\downloads from chrome\logo.ico")

# creating Scrollbar
sb = Scrollbar(top)
sb.pack(side=RIGHT, fill=Y)

# creating a text area
textarea = Text(top, yscrollcommand=sb.set, height=756, width=1024)
textarea.pack()
sb.config(command=textarea.yview)

# creating radio button in format  menu
check = IntVar()


def browse_file():
    global browse_file
    browse_file = filedialog.askopenfilename()


def newFile():
    global file
    top.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "."),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        top.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "."),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            top.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def cut():
    textarea.event_generate("<>")


def copy():
    textarea.event_generate("<>")


def paste():
    textarea.event_generate("<>")


def undo():
    textarea.event_generate("<>")


def delete():
    textarea.event_generate("<>")


def about():
    tkinter.messagebox.showinfo("Notepad", "Notepad by Anjali Kumari")


def date_time():
    print(time.asctime())


menubar = Menu(top)
# creating File Menu
file = Menu(menubar, tearoff=0)
file.add_command(label="New                             Ctrl+N", command=newFile)
file.add_command(label="New Window       Ctrl+Shift+N")
file.add_command(label="Open...                        Ctrl+O", command=browse_file)
file.add_command(label="Save                            Ctrl+S", command=saveFile)
file.add_command(label="Save as...               Ctrl+Shift+S")
file.add_separator()
file.add_command(label="Page Setup...")
file.add_command(label="Print...                         Ctrl+P")
file.add_separator()
file.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=file)

# creating File Menu
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo                                   Ctrl+Z", command=undo)
edit.add_separator()
edit.add_command(label="Cut                                      Ctrl+X", command=cut)
edit.add_command(label="Copy                                    Ctrl+C", command=copy)
edit.add_command(label="Paste                                    Ctrl+V", command=paste)
edit.add_command(label="Delete                                    Del", command=delete)
edit.add_separator()
edit.add_command(label="Search with Bing...             Ctrl+E")
edit.add_command(label="Find...                                   Ctrl+F")
edit.add_command(label="Find Next                                 F3")
edit.add_command(label="Find Previous                     Shift+F3")
edit.add_command(label="Replace...                            Ctrl+H")
edit.add_command(label="Go To...                                Ctrl+G")
edit.add_separator()
edit.add_command(label="Select All                              Ctrl+A")
edit.add_command(label="Time/Date                                F5", command=date_time)
menubar.add_cascade(label="Edit", menu=edit)

# Creating Format menu
Format = Menu(menubar, tearoff=0)
Format.add_radiobutton(label="Word wrap", variable=check, value=1)
Format.add_radiobutton(label="Font", variable=check, value=2)
menubar.add_cascade(label="Format", menu=Format)

# Creating View menu

View = Menu(menubar, tearoff=0)
# Adding sub_menu in Zoom
sub_menu = Menu(View, tearoff=0)
sub_menu.add_command(label="Zoom in                                   Ctrl+Plus")
sub_menu.add_command(label="Zoom Out                                Ctrl+Minus")
sub_menu.add_command(label="Restore Default Zoom            Ctrl+0")

# Creating Zoom option
View.add_cascade(label="Zoom", menu=sub_menu)
View.add_checkbutton(label="Status Bar", onvalue=1, offvalue=0)
menubar.add_cascade(label="View", menu=View)

# def about_us():
#     root = Toplevel(top)
#     root.title("About Notepad")
#     # root.iconbitmap("D:\downloads from chrome\logo.ico")
#     root.geometry("500x400")
#     btn = Button(root, text="OK", command=quit)
#     btn.place(x=6, y=80)


# Creating help menu
help = Menu(menubar, tearoff=0)
help.add_command(label="View Help")
help.add_command(label="Send Feedback")
help.add_separator()
help.add_command(label="About Notepad", command=about)
menubar.add_cascade(label="Help", menu=help)
top.config(menu=menubar)

top.mainloop()
