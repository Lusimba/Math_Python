numbers = [1,2,3,4,5,6]
def greater_than_three(x):
    return x>3
print(list(filter(greater_than_three,numbers)))
# no need for function in this code    
print(list(filter(lambda x: x>3,numbers)))