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

#