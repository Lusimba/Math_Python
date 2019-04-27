from tkinter import *

root = Tk()
photo = PhotoImage(file="E:\LI_code\Math_Python\Tkinter\Images\daenerys.png")
label = Label(root, image = photo, height=400, width = 600)
label.pack()

root.mainloop()