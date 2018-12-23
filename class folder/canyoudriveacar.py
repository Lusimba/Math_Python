def canyoudrive():
    x = input("what is your name: ")
    y = int(input("what is your age: "))
    if y >= 18:
        return "you can drive a car"
    else:
        return "you cannot drive a car"   
print(canyoudrive())        