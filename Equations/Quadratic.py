#A quadratic equation is of the form ax+by+c
#To find the roots, we use the quadratic formula. 
#We shall take the parameters a, b, and c from the user to find x1 and x2. 
# import math
a = float(input('Enter coeff a: '))
b = float (input('Enter coeff b: '))
c = float (input('Enter coeff c: '))
def roots (a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    # print('The roots of %fx+%f+%f is %0.2f and %0.2f' %f(a, b, c, x1, x2))
    print('The roots of %sx+%s+%s are %s and %s'%(a, b, c, x1, x2))
    return roots
roots (a, b, c)
