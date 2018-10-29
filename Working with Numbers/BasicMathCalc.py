# A program that prints 
x = int(input('Enter the first number'))
y = int(input('Enter the second number'))

#Addition
def add (x, y):
    return x+y
#Subtraction
def subtract (x, y):
    return x-y
#Multiplication
def multiply (x, y):
    return x*y
#Division
def divide (x, y):
    return x/y
#Floor division
def floor (x, y):
    return x // y
#Modulo operation
def modulo (x, y):
    return x % y
#Exponential
def exp (x, y):
    return x ** y
#Evaluate User input and determine the appropriate function
ans = input('Type the desired operation: \n add, \n subtract, \n multiply, \n modulo, \n divide, \n exp, or \n floor \n')
if ans == 'add':
    print(add(x, y))
if ans == 'subtract':
    print(subtract(x, y))
if ans == 'multiply':
    print(multiply(x, y))
if ans == 'divide':
        print(divide(x, y))
if ans == 'floor':
    print(floor(x, y))
if ans == 'modulo':
    print(modulo(x, y))
if ans == 'exp':
    print(exp(x, y))
#Extract and display the type of the output 'ans'
print (type(ans))