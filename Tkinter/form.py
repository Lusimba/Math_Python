from tkinter import *

window=Tk() # labels tkinter as window
window.geometry("500x500")
window.title("Registration Form")

#define functions
def console():
    print("Created a submit form")

def exit1():
    exit()
#Main program goes here

label1 = Label(window, text="Registration Form", relief = "solid", width = 20, font = ("arial", 19, "bold"))
label1.place(x = 90, y = 53)

label2 = Label(window, text="FirstName",  width = 20, font = ("arial", 12, "bold"))
label2.place(x = 80, y = 130)

label1 = Label(window, text="LastName", width = 20, font = ("arial", 12, "bold"))
label1.place(x = 80, y = 179)

b1 = Button(window, text = "Login", bg = 'brown', fg='white', command=console)
b1.place(x = 150, y=380)

b1 = Button(window, text = "Exit", bg = 'brown', fg='white', command=exit1)
b1.place(x = 280, y=380)

#End of main program
window.mainloop()