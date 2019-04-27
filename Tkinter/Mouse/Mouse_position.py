from tkinter import *
     
def showPosEvent(event):
    print ("Widget=%s X=%s Y=%s".format(event.widget, event.x, event.y))
     
def onRightClick(event):
    print ('Got right mouse button click:') 
    showPosEvent(event)
     
tkroot = Tk()
labelfont = ('courier', 20, 'bold')                
widget = Label(tkroot, text='Hello bind world')
widget.config(bg='red', font=labelfont)            
widget.config(height=5, width=20)                  
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Button-1>',  onRightClick)

widget.focus()                                     
tkroot.title('Click Me')
tkroot.mainloop()