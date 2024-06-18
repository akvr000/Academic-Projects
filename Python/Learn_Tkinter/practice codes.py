import customtkinter
import tkinter.messagebox

root = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root.geometry("400x400+120+70")
root.minsize(600, 450)
root.title("Demo")
root.configure(background="#856ff8")

# root.iconbitmap(r"D:\downloads from chrome\logo.ico")


def log_in():
    print("logged in successfully")
    print(f"your username is {userentry.get()}")
    print(f"your username is {passentry.get()}")
    tkinter.messagebox.showinfo(title="Login Successful", message="You have logged in Successfully!")


# creating frame

form = customtkinter.CTkFrame(root, width=500, height=900)
form.pack(fill="y", pady=40, padx=40)

# Heading
heading = customtkinter.CTkLabel(form, text="Log in to your account")
heading.pack(pady=30, padx=100)

# creating Entries

userentry = customtkinter.CTkEntry(form, placeholder_text="Username")
userentry.pack()
passentry = customtkinter.CTkEntry(form, placeholder_text="Password", show="*")
passentry.pack(pady=10)

button = customtkinter.CTkButton(form, text="Log in", command=log_in)
button.pack(pady=16)

check = customtkinter.CTkCheckBox(form, text="remember me")
check.pack(pady=12)

root.mainloop()
