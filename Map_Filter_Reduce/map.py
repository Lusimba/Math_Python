#The map function is used to apply an action to elements in a list or array without
#altering the original list, hence resulting in pure functions without side effects.
# numbers = [1, 2, 3, 4, 5]
# def square (x):
#     return x**2
# print(list(map(square,numbers))) 
# print(list(map(lambda x: x**2, numbers))) 
#We can also use lambda functions to represent the above equation as follows:
#print('When we use lambda, the map function returns the values below: ')


# #We can also use the map function with strings. 
def uppercase(string):
    return string.upper()
values = ['abc', 'def', 'ghi']

print(list(map(uppercase, values)))


