from tkinter import *


def navbar(root, text_color, color2, color3, command_switch, home_cmd, faq_cmd, call_cmd, shop_cmd, camera_cmd, arrow, arrow_rev, home, call, camera, msg, shop):

    global navRoot
    global arrow_button
    global closeBtn

    # setting moving Navbar frame:
    navRoot = Frame(root, bg=color2, height=1000, width=300)
    navRoot.place(x=-300, y=0)

    # setting static Navbar frame:
    navStatic = Frame(root, bg=color2, height=1000, width=70)
    navStatic.place(x=0, y=0)

    # Setting Up logo labels in the 2 frames.
    logo_label1 = Label(navRoot, font="Bahnschrift 15",
                        bg=color3, fg="black", height=3, width=300, padx=20)
    logo_label2 = Label(navStatic, font="Bahnschrift 15",
                        bg=color3, fg="black", height=3, width=60, padx=20)

    logo_label1.place(x=0, y=0)
    logo_label2.place(x=0, y=0)

    # arrow-button of static
    arrow_button = Button(logo_label2, image=arrow, bg=color3,
                          activebackground=color3, command=command_switch, bd=0)
    # arrow-button of moving
    # Navbar Close Button:
    closeBtn = Button(navRoot, image=arrow_rev,
                      bg=color3, activebackground=color3, bd=0, command=command_switch)

    arrow_button.place(x=20, y=25)
    closeBtn.place(x=250, y=27)

    # nav-items-------------------------------------------------------------------------------------

    # --nav labels
    nav_label1 = Label(navStatic, font="Bahnschrift 15",
                       bg=color2, fg="black", height=2, width=60, padx=20)
    nav_label2 = Label(navStatic, font="Bahnschrift 15",
                       bg=color2, fg="black", height=2, width=60, padx=20)
    nav_label3 = Label(navStatic, font="Bahnschrift 15",
                       bg=color2, fg="black", height=2, width=60, padx=20)
    nav_label4 = Label(navStatic, font="Bahnschrift 15",
                       bg=color2, fg="black", height=2, width=60, padx=20)
    nav_label5 = Label(navStatic, font="Bahnschrift 15",
                       bg=color2, fg="black", height=2, width=60, padx=20)

    nav_label1.place(x=0, y=120)
    nav_label2.place(x=0, y=220)
    nav_label3.place(x=0, y=320)
    nav_label4.place(x=0, y=420)
    nav_label5.place(x=0, y=610)

    # --nav buttons
    home_button = Button(nav_label1, image=home, bg=color2,
                         activebackground=color2, bd=0, command=home_cmd)
    faq_button = Button(nav_label2, image=msg, bg=color2,
                        activebackground=color2, bd=0, command=faq_cmd)
    call_button = Button(nav_label3, image=call, bg=color2,
                         activebackground=color2, bd=0, command=call_cmd)
    shop_button = Button(nav_label4, image=shop, bg=color2,
                         activebackground=color2, bd=0, command=shop_cmd)
    camera_button = Button(nav_label5, image=camera, bg=color2,
                           activebackground=color2, bd=0, command=camera_cmd)

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
            Label(navRoot, text=options[i], font="BahnschriftLight 15", bg=color2, fg=text_color,
                  bd=0).place(x=75, y=625)
        else:
            Label(navRoot, text=options[i], font="BahnschriftLight 15", bg=color2, fg=text_color,
                  bd=0).place(x=75, y=y)
            y += 100
