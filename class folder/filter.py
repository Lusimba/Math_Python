numbers = [1,2,3,4,5,6]
def greater_than_three(x):
    return x>3
print(list(filter(greater_than_three,numbers)))    
print(list(filter(lambda x: x>3,numbers)))