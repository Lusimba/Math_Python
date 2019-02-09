class driver:
    #instance method
    def age(self, x):
        if(x>=18):
            print('You can drive a vehicle in India')
        else:
            print('Sorry, you need to be at least 18 years of age!')
    #class Method
    @classmethod
    def interest(cls,x):
        x*=1.5
        print('Your new age is {}'.format(x))
x=int(input('What is your age?'))
driving = driver()
driving.age(x)
driving.interest(x)