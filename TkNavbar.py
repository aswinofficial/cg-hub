from tkinter import *

#--background-colors 👇

Bg_1 = "#34343B"
Bg_2 = "#23232E"
Bg_3 = "#141418"


#--text-colors 👇

Button_txt = "#FFFFFF"
Card_txt = "#000000"
Title_txt = "#777778"

#--extra-colors 👇

Share_button = "#04F0FF"
Card = "#C4C4C4"


root = Tk()
root.geometry("1167x667")
root.config(bg=Bg_1)
root.resizable(0,0)







# dictionary of colors:
color = {"nero": Bg_1, "orange": Button_txt, "darkorange": Button_txt}

# setting root window:


# setting switch state:
btnState = False

# loading Navbar icon image:
"""navIcon = PhotoImage(file="menu.png")
closeIcon = PhotoImage(file="close.png")"""

# setting switch function:


def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(311):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="#FA0583")
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(10, 311):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True


# top Navigation bar:
topFrame = Frame(root, bg=color["orange"])
topFrame.pack(side="top", fill=X)

# Header label text:
homeLabel = Label(topFrame, text="Share", font="Bahnschrift 15",
                     bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
brandLabel = Label(root, text="Cherry\nCodes🍒",
                      font="System 30", bg="gray17", fg="#FA0583")
brandLabel.place(x=100, y=250)

# Navbar button:
navbarBtn = Button(topFrame, text="Nav",
                      bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
navbarBtn.place(x=100, y=10)

# setting Navbar frame:
navRoot = Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=10, y=0)
Label(navRoot, font="Bahnschrift 15",
         bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Profile", "Settings", "Help", "About", "Feedback"]
# Navbar Option Buttons:
for i in range(5):
    Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"],
              activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = Button(navRoot, text="Close",
                     bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=250, y=10)

# window in mainloop:
root.mainloop()
