import time
y = time.time()
x = int(input("Please enter a number: "))
def countdown(number):
    if number == 0:
        print("compete")
    else:
        print(number) 
        countdown(number-1)
countdown(x)  
w = time.time()
print(w-y)         