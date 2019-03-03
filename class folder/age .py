class canyoudriveacar(object):
    def age(self, x):
        if x>=18:
            print("You can drive a vehical in India")
        else:
            print("Sorry ,you ain't alowwed !!!!!!!!idiot")
    @classmethod
    def interest(cls, x):
        x*=1.5
        print("Your new age is {}".format(x))       
x = int(input("Please enter your age: "))
driving = canyoudriveacar()
driving.age(x)  
driving.interest(x)

