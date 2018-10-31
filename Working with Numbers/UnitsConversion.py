#Distance
#Inches to Metres
#1 inch = .0254 meters

x = float(input('Enter your number in inches: '))
conv = 0.0254
def distance(x, conv):
    output = x*conv
    print('{} inches is equal to {} metres'.format (x, output))
    return distance
distance(x, conv)


#You can use a similar method to convert any other units of measurement of distance
#Temperature
#The conversion from Fahrenheit to Celsius and Celsius to Kelvin

F= float(input('enter a temperature value in fahrenheit: '))
def celsius(F):
    c = (F - 32)*(5/9)
    print('{0} degrees Fahrenheit is {1} degrees Celcius'.format(F, c))
    return celsius
celsius(F)

#Celsius to Kelvin Conversion
#Use the float formatter %0.2f to limit the decimal numbers to 2 places

c = float(input('Enter a temperature in Celsius: '))
def Kelvin (c):
    K = c+273
    print('%s degrees Celsius is %0.2f Kelvin' %(c, K))
Kelvin(c)
