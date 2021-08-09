from tkinter import *
import home as h
import navbar as nav

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
neo = PhotoImage(file="images/neo.png")

# setting switch state:
btnState = False


# setting switch function:


def switch():
    global btnState
    nav.navRoot.destroy()
    nav.navbar(root, Title_txt, Bg_2, Bg_3, switch, home_tab,
               faq_tab, call_tab, shop_tab, cam_tab, arrow, arrow_rev, home, call, camera, msg, shop)
    if btnState is True:

        nav.closeBtn.config(image="")

        # create animated Navbar closing:
        for x in range(301):
            nav.navRoot.place(x=-x, y=0)
            nav.navRoot.update()

        # resetting widget colors and images:
        nav.arrow_button.config(image=arrow)
        """pagetitle.place(x=60, y=24)
        share_button.config(bg=Bg_1)"""

        root.config(bg=Bg_1)

        # turning button OFF:
        btnState = False
    else:
        # make root dim and arrow gone and reverse arrow appear:
        # also making the title vanish :

        nav.arrow_button.config(image="")
        nav.closeBtn.config(image=arrow_rev)
        """share_button.config(bg="grey")
        pagetitle.place_forget()"""

        root.config(bg="grey")

        # created animated Navbar opening:
        for x in range(-300, 0):
            nav.navRoot.place(x=x, y=0)
            nav.navRoot.update()

        # turing button ON:
        btnState = True


def home_tab():
    h.title(root, "Home", Bg_1, share)
    h.home(root, 100, 10)


def faq_tab():
    pass


def call_tab():
    pass


def shop_tab():
    pass


def cam_tab():
    pass

# NAV BAR 👇


nav.navbar(root, Title_txt, Bg_2, Bg_3, switch, home_tab,
           faq_tab, call_tab, shop_tab, cam_tab, arrow, arrow_rev, home, call, camera, msg, shop)

# window in mainloop:
root.mainloop()
