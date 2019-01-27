#The filter function is inbuilt in Python. It applies evaluates and returns elements
# in a list that satisfy a particular criteria.
numbers = [1, 2, 3, 4, 5,6]

def greater_than_three(x):
    return x>3
    
print(list(filter(lambda x: x>3,numbers)))