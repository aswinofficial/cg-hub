from tkinter import *


def home(root, x, y):
    Frame(root, width=20, height=300, bg="black", bd=0).place(x=x, y=y)


def title(root, title, color, img):
    # Title label
    pagetitle = Label(root, text=title, font=("arial bold", 20),
                      bg=color, fg="white", bd=0, padx=20)
    pagetitle.place(x=60, y=24)

    # Share label
    share_button = Button(root, image=img, activebackground=color,
                          bg=color, fg="gray17", padx=20, bd=0)
    share_button.place(x=1053, y=17)
