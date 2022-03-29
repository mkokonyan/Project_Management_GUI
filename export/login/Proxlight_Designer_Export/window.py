from tkinter import *


def btn_clicked():
    print("Button Clicked")

def login_btn_on_enter(e):
    b1["image"] = img2


def login_btn_on_leave(e):
    b1["image"] = img1


def create_btn_on_enter(e):
    b0["image"] = img3
    b0["cursor"] = "hand2"
    b0.place(
        x=1231, y=901.2,
        width=57,
        height=22)


def create_btn_on_leave(e):
    b0["image"] = img0



window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#f9f4f5")
canvas = Canvas(
    window,
    bg = "#f9f4f5",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
img3 = PhotoImage(file = f"img3.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    background="#F9F4F5",
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 1231, y = 903,
    width = 57,
    height = 22)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    263.5, 768.0,
    image=background_img)

img1 = PhotoImage(file = f"img1.png")
img2 = PhotoImage(file = f"img2.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    background="#E0E0E0",
    activebackground="#e0e0e0",
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 1049, y = 680,
    width = 250,
    height = 81)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    1188.0, 480.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e0e0e0",
    font = ("Helevetica neue", 16),
    highlightthickness = 0)

entry0.place(
    x = 1039, y = 463,
    width = 298,
    height = 32)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    1188.0, 610.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e0e0e0",
    font=("Helevetica neue", 16),
    highlightthickness = 0)

entry1.place(
    x = 1039, y = 593,
    width = 298,
    height = 32)


b0.bind("<Enter>", create_btn_on_enter)
b0.bind("<Leave>", create_btn_on_leave)
b1.bind("<Enter>", login_btn_on_enter)
b1.bind("<Leave>", login_btn_on_leave)



window.resizable(False, False)
window.mainloop()
