import os
import random

dyrectory = "C:\\Users\maced\PycharmProjects\VANAR\OOP\img-PIL\IMG\\"
files = os.listdir(dyrectory)
print(files)

from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()


tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Мое приложение")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
#tk.iconbitmap("bomb-3175208_640.ico")

canvas = Canvas(tk, width=600, height=600, bg="red", highlightthickness=0)
canvas.pack()

# canvas.create_oval(100, 100, 300, 300, fill="yellow", outline="")
# canvas.create_oval(120, 120, 280, 280, fill="white", outline="")
#
# canvas.create_rectangle(400,100,500,500, fill="lightgreen")
# canvas.create_rectangle(420,120,480,480, fill="darkgreen", outline="")
#
# canvas.create_text(200,500,text="Hello World!", font=("Arial", 40),fill="white")


random.shuffle(files)

for img in files:
    img_obj = Image.open(dyrectory+img)
    box = 500
    wide_size = (box/float(img_obj.size[0]))
    height_size = int((float(img_obj.size[1])*float(wide_size)))
    img_obj = img_obj.resize((box, height_size), Image.ANTIALIAS)
    img_obj = ImageTk.PhotoImage(img_obj)
    our_label2 = Label(image=img_obj)
    our_label2.image = img_obj
    our_label2.place(x=random.randint(0, 600), y=random.randint(0, 400))

tk.mainloop()


