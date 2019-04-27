x = input("Please eneter a string: ")
x = x.lower()
b = x[::-1]
if x == b:
    print("the word is a pallindrom")
    print("when reversed it is ",b)
else:
    print("the word is not a pallindrom")
