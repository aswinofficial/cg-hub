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

Share_but = "#04F0FF"
Card = "#C4C4C4"


root = Tk()
root.title("CG-HUB")
root.iconbitmap("images/logo.ico")
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
        for x in range(301):
            navRoot.place(x=-x, y=0)
            navRoot.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="#FA0583")
        share_button.config(bg=color["orange"])
        
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        share_button.config(bg=color["nero"])
        
        root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            navRoot.update()

        # turing button ON:
        btnState = True



# Header label text:
share_button = Button(root, text="Share", font="Bahnschrift 15",
                     bg=color["orange"], fg="gray17", height=2, padx=20,bd=0)
share_button.place(x=1053, y=10)

# Main label text:
brandLabel = Label(root, text="Cherry\nCodes🍒",
                      font="System 30", bg="gray17", fg="#FA0583")
brandLabel.place(x=100, y=250)

# Navbar button:
pagetitle = Label(root, text="Home", font=("arial bold",20),
                      bg=Bg_1, fg="white", bd=0, padx=20)
pagetitle.place(x=60, y=10)

# setting Navbar frame:
navRoot = Frame(root, bg="red", height=1000, width=300)
navRoot.place(x=-300, y=0)
Label(navRoot, font="Bahnschrift 15",
         bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)


navStatic = Frame(root, bg="blue", height=1000, width=70)
navStatic.place(x=0, y=0)
logo_label = Label(navStatic, font="Bahnschrift 15",
         bg=color["orange"], fg="black", height=3, width=60, padx=20).place(x=0, y=0)


# logo button

logo_button = Button(logo_label,text="Nav",fg="black",command=switch,bd=0).place(x=17,y=10)


# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Profile", "Settings", "Help", "About", "Feedback"]
# Navbar Option Buttons:
for i in range(5):
    Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"],
              activebackground="gray17", activeforeground="green", bd=0).place(x=75, y=y)
    y += 40

# Navbar Close Button:
closeBtn = Button(navRoot, text="Close",
                     bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=250, y=10)

# window in mainloop:
root.mainloop()
