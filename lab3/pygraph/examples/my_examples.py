
from tkinter import *
import time
root = Tk()
root.title("Let's smile!")
countdown = 4
txt = "Smile at "
bg = Label(master=root, bg="black", fg="white", font="Arial 70", text=txt + str(countdown))
bg.pack()
def starting(ev):
    global txt, countdown
    if ev == "Enter":
        while countdown != 0:
            time.sleep(0.5)
            countdown -= 1
            bg["text"] = txt + str(countdown)
            bg.update()
            time.sleep(1)
        bg["text"] = "Done!"
root.bind("Space", starting(ev="Enter"))
root.mainloop()
