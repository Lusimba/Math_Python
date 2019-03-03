class driver():
    @staticmethod
    def age(x):
        if x>=18:
            print("you are free to drive a car in india.")
        else:
            print("you are not alowed to drive a car in India")
driving = driver()
x = int(input("what is your age: "))
driving.age(x)                

