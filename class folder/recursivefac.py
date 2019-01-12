x = int(input("please enter a number: "))
def factorial(number):
    if number == 1:
        print("complete")
        return 1
    else:
        y = number*factorial(number-1) 
        return y
print(factorial(x) )
          