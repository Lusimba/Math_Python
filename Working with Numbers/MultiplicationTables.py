'''
We will print a multiplication table using python
10x10
'''

def multTable(a):
    for i in range (1, 11):
        print ('{0} x {1} = {2}'.format (a, i, a*i))
if __name__ == '__main__':
        a = input('Enter a number: ')
multTable(float(a))

#We can create a multiplication table for odd numbers only ass below

def multTableOdd(a):
    for i in range (1, 11, 2):
        print ('{0} x {1} = {2}'.format (a, i, a*i))
if __name__ == '__main__':
        a = input('Enter a number: ')
multTableOdd(float(a))

#We can also create one for even numbers only

def multTableEven(a):
    for i in range (2, 11, 2):
        print ('{0} x {1} = {2}'.format (a, i, a*i))
if __name__ == '__main__':
        a = input('Enter a number: ')
multTableEven(float(a))

