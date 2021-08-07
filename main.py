from tkinter import *


# --background-colors 👇

Bg_1 = "#34343B"
Bg_2 = "#23232E"
Bg_3 = "#141418"


# --text-colors 👇

Button_txt = "#FFFFFF"
Card_txt = "#000000"
Title_txt = "#777778"

# --extra-colors 👇

Share_but = "#04F0FF"
Card = "#C4C4C4"


# setting root window:

root = Tk()
root.title("CG-HUB")
root.iconbitmap("images/logo.ico")
root.geometry("1167x667")
root.config(bg=Bg_1)
root.resizable(0, 0)


# --images/icons

arrow = PhotoImage(file="images/arrow1.png")
arrow_rev = PhotoImage(file="images/arrow2.png")
home = PhotoImage(file="images/home.png")
call = PhotoImage(file="images/call.png")
camera = PhotoImage(file="images/camera.png")
msg = PhotoImage(file="images/msg.png")
shop = PhotoImage(file="images/shop.png")
share = PhotoImage(file="images/share.png")

# setting switch state:
btnState = False


# setting switch function:


def switch():
    global btnState
    if btnState is True:

        closeBtn.config(image="")

        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            navRoot.update()

        # resetting widget colors and images:
        arrow_button.config(image=arrow)
        brandLabel.config(bg=Bg_1, fg="#FA0583")
        pagetitle.place(x=60, y=24)
        share_button.config(bg=Bg_1)

        root.config(bg=Bg_1)

        # turning button OFF:
        btnState = False
    else:
        # make root dim and arrow gone and reverse arrow appear:
        # also making the title vanish :
        pagetitle.place_forget()
        arrow_button.config(image="")
        closeBtn.config(image=arrow_rev)
        share_button.config(bg="grey")
        brandLabel.config(bg="grey", fg="#5F5A33")

        root.config(bg="grey")

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            navRoot.update()

        # turing button ON:
        btnState = True


# Title label
pagetitle = Label(root, text="Home", font=("arial bold", 20),
                  bg=Bg_1, fg="white", bd=0, padx=20)
pagetitle.place(x=60, y=24)


# Share label
share_button = Button(root, image=share,
                      bg=Bg_1, fg="gray17", padx=20, bd=0)
share_button.place(x=1053, y=17)

# Main label text:
brandLabel = Label(root, text="Cherry\nCodes🍒",
                   font="System 30", bg=Bg_1, fg="#FA0583")
brandLabel.place(x=500, y=250)


# setting Navbar frame:
navRoot = Frame(root, bg=Bg_2, height=1000, width=300)
navRoot.place(x=-300, y=0)
logo_label1 = Label(navRoot, font="Bahnschrift 15",
                    bg=Bg_3, fg="black", height=3, width=300, padx=20)
logo_label1.place(x=0, y=0)


navStatic = Frame(root, bg=Bg_2, height=1000, width=70)
navStatic.place(x=0, y=0)


logo_label2 = Label(navStatic, font="Bahnschrift 15",
                    bg=Bg_3, fg="black", height=3, width=60, padx=20)
logo_label2.place(x=0, y=0)


# arrow-button of static

arrow_button = Button(logo_label2, image=arrow, bg=Bg_3,
                      activebackground=Bg_3, command=switch, bd=0)
arrow_button.place(x=20, y=25)


# nav-items

# --nav labels
nav_label1 = Label(navStatic, font="Bahnschrift 15",
                   bg=Bg_2, fg="black", height=2, width=60, padx=20)
nav_label2 = Label(navStatic, font="Bahnschrift 15",
                   bg=Bg_2, fg="black", height=2, width=60, padx=20)
nav_label3 = Label(navStatic, font="Bahnschrift 15",
                   bg=Bg_2, fg="black", height=2, width=60, padx=20)
nav_label4 = Label(navStatic, font="Bahnschrift 15",
                   bg=Bg_2, fg="black", height=2, width=60, padx=20)
nav_label5 = Label(navStatic, font="Bahnschrift 15",
                   bg=Bg_2, fg="black", height=2, width=60, padx=20)


nav_label1.place(x=0, y=120)
nav_label2.place(x=0, y=220)
nav_label3.place(x=0, y=320)
nav_label4.place(x=0, y=420)
nav_label5.place(x=0, y=610)


# --nav buttons
home_button = Button(nav_label1, image=home, bg=Bg_2,
                     activebackground=Bg_2, bd=0)
faq_button = Button(nav_label2, image=msg, bg=Bg_2,
                    activebackground=Bg_2, bd=0)
call_button = Button(nav_label3, image=call, bg=Bg_2,
                     activebackground=Bg_2, bd=0)
shop_button = Button(nav_label4, image=shop, bg=Bg_2,
                     activebackground=Bg_2, bd=0)
camera_button = Button(nav_label5, image=camera, bg=Bg_2,
                       activebackground=Bg_2, bd=0)


home_button.place(x=8, y=0)
faq_button.place(x=8, y=0)
call_button.place(x=8, y=0)
shop_button.place(x=8, y=0)
camera_button.place(x=8, y=0)

# set y-coordinate of Navbar widgets:
y = 140
# option in the navbar:
options = ["Home", "FAQ", "Contact Us", "Shop", "Capture"]
# Navbar Option Buttons:
for i in range(5):
    if i == 4:
        Label(navRoot, text=options[i], font="BahnschriftLight 15", bg=Bg_2, fg=Title_txt,
              bd=0).place(x=75, y=625)
    else:
        Label(navRoot, text=options[i], font="BahnschriftLight 15", bg=Bg_2, fg=Title_txt,
              bd=0).place(x=75, y=y)
        y += 100

# Navbar Close Button:
closeBtn = Button(navRoot, image=arrow_rev,
                  bg=Bg_3, activebackground=Bg_3, bd=0, command=switch)
closeBtn.place(x=250, y=27)

# window in mainloop:
root.mainloop()
