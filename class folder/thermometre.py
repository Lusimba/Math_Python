class thermometer(object):
    def temperature(self, x):
        if x > 38 and x < 36:
            print("you are unhealthy!!!!!!!!!!!!~!!") 
        else:
            print("you are fine") 
x = float(input("what is your body temp: "))
temp = thermometer()
temp.temperature(x)                  