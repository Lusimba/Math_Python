def leep():
    z = int(input("please enter a year: "))
    if z%4 == 0:
        return "the year you entered is a leep year"
    else:
        return "the year you entered is not a leep year"    
print(leep())        