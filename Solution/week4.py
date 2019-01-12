# 4.1
def maxnumber():
    x = int(input("please enter a number: "))
    y = int(input("please enter a number: "))
    z = int(input("please enter a number: "))
    return "the max the numbers you enter is ",max(x,y,z)
print(maxnumber()) 
print("                        -                           ")   

#4.2
alist = []
def sum1():
    a = int(input("please enter a number: "))
    alist.append(a)
    b = int(input("please enter a number: "))
    alist.append(b)
    c = int(input("please enter a number: "))
    alist.append(c)
    sum = 0
    for counter in alist:
        sum = sum + counter
    return "the sum of the numbers that you entered is ",sum
print(sum1())
print("                        -                           ")   

#4.3    
blist = []
def multiply():
    d = int(input("please enter a number: "))
    blist.append(d)
    e = int(input("please enter a number: "))
    blist.append(e)
    f = int(input("please enter a number: "))
    blist.append(f)
    mul = 1
    for counter in blist:
        mul = mul * counter
    return "the product of the numbers that you entered is ",mul
print(multiply())
print("                        -                           ")   

#4.4
i = input("pleae enter a string: ")
print("the reverse of your string is: ",i[::-1])
print("                        -                           ")   

#4.5
def factorial():
    g = int(input("Please enter a number: "))
    factorial = 1
    for counter in range(1,g+1):
        factorial = factorial * counter
    return "the factorial is ",factorial    
print(factorial())
print("                        -                           ")   

#4.6
def findrange():
    h = int(input("please enter the first number: "))
    i = int(input("please enter the second number: "))
    j = int(input("enter a number to find if it is in the range of the first and second number: "))
    if h <= j <= i:
        return "the number is in given range"
    else:
        return "the number is not in the given range"
print(findrange())
print("                        -                           ")   

#4.7
upperlist = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W"\
,"X","Y","Z"]
lowerlist = ["a","b","c","d","e","g","h","i","j","f","k","l","m","n","o","p","q","r","s","t","u","v","w"\
,"x","y","z"]
def upperlower():
    k = input("please enter a word: ")
    upper = 0
    lower = 0
    for counter in upperlist:
        for counter2 in k:
            if counter == counter2:
                upper = upper + 1
    for count in lowerlist:
        for count2 in k:
            if count == count2:
                lower = lower + 1 
    return "the lower letters are ",lower," and upper ",upper
print(upperlower())
print("                        -                           ")       

#4.8
nlist = []
ulist = []
def change():
    l = int(input("Please enter a number : "))
    m = int(input("Please enter another number(you can repeat your numbers): "))
    n = int(input("Please enter another number(you can repeat your numbers): "))
    o = int(input("Please enter another number(you can repeat your numbers): "))
    p = int(input("Please enter another number(you can repeat your numbers): "))
    q = int(input("Please enter another number(you can repeat your numbers): "))
    r = int(input("Please enter another number(you can repeat your numbers): "))
    s = int(input("Please enter another number(you can repeat your numbers): "))
    nlist.append(l)
    nlist.append(m)
    nlist.append(n)
    nlist.append(o)
    nlist.append(p)
    nlist.append(q)
    nlist.append(r)
    nlist.append(s)
    for counter in nlist:
        for counter2 in ulist:
            if counter != counter2:
                ulist.append(counter)
    return "the unique list is ",ulist
print(change())   
print("                        -                           ")       

#4.9
def primecomposit():
    t = int(input("please neter a number: "))   
    for counter in range(1,t+1):
        cs = 0 
        if counter % t == 0:
            return "the number that you entered is a composite number"
            cs = 1
            break
    if cs != 1:
        return "the number that you entered is a prime number"        
print(primecomposit())   
print("                        -                           ")       

#4.11
factorlist = []
def perfect ():
    u = int(input("please enter a number to find if it is perfect or not: "))
    for counter in range(1,u+1):
        if counter%u==0:
            factorlist.append(counter)
    add = 0        
    for counter2 in factorlist:
        add = add + counter2
    if add == u:
        return "the number is a perfect number"
    else:
        return "the number is not a perfect number"
print(perfect())
print("                        -                           ")       


from tkinter import *
expression = "" 
def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 
def equalpress(): 
    try:
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = "" 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
if __name__ == "__main__": 
    gui = Tk() 
    gui.configure(background="light green") 
    gui.title("Simple Calculator")  
    gui.geometry("00x300") 
    equation = StringVar()  
    expression_field = Entry(gui, textvariable=equation) 
    expression_field.grid(columnspan=4, ipadx=70) 
  
    equation.set('enter your expression')  
    button1 = Button(gui, text=' 1 ', fg='green', bg='blue', 
                     command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(gui, text=' 2 ', fg='green', bg='blue', 
                     command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='green', bg='blue', 
                     command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='green', bg='blue', 
                     command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='green', bg='blue', 
                     command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='green', bg='blue', 
                     command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='green', bg='blue', 
                     command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='green', bg='blue', 
                     command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='green', bg='blue', 
                     command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='green', bg='blue', 
                     command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ', fg='green', bg='blue', 
                  command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', fg='green', bg='blue', 
                   command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' * ', fg='green', bg='blue', 
                      command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text=' / ', fg='green', bg='blue', 
                    command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', fg='green', bg='blue', 
                   command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
  
    clear = Button(gui, text='Clear', fg='green', bg='blue', 
                   command=clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
    gui.mainloop()