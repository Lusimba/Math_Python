from tkinter import *

my_window = Tk()
my_canvas = Canvas(my_window, width = 400, height = 400, background = 'white')
my_canvas.grid(row= 0, column=0)
my_canvas.create_line(100, 100, 300, 100, 200, 300, 100, 100, fill = 'blue', width = 5)
my_window.mainloop()





















