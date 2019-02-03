numbers = [1,2,3,4,5]
def square(x):
    return x**2
print(list(map(square,numbers)))
print(list(map(lambda x: x**2,numbers)))    