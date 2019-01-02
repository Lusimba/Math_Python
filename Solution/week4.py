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

#4.11