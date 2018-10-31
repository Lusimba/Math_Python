#python supports complex numbers as a + bj

a = 2 + 3j
x = a.imag
y = a.real
z = a.conjugate()
u = abs(a)
print (a)
print ('The real part of the above number is %s'%(y))
print ('The imaginary part of the above number is {}'.format(x))
print ('The conjugate of the above number is {}'.format(z))
print ('The absolute value of the above number is {}'.format(u))
