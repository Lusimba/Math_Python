
class Bus():
    availableSeats=0
    def __init__(self,destination,departureTime,arrivalTime,seats,price):
        self.start = "Hyderabad"
        self.destination = destination
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.seats = seats
        self.availableSeats = seats
        self.price = price
    def seatBlock(self):
        self.availableSeats=self.availableSeats-1
class TravelSystem():
    delhiBus = Bus("Delhi","08:30 AM","11:00 PM", 32,2570)    
    mumbaiBus = Bus("Mumbai","09:00 AM","12:30 PM", 32,1150)    
    chennaiBus = Bus("Chennai","9:30 AM","11:00 PM", 32,1800)    
    puneBus = Bus("Pune","10:00 AM","11:00 PM", 32,1950)    
    def printTicket(self,place,name):
        if place == 1:
            print("Hi ",name, ", You are going to Delhi ,at 8:30 AM,you will reach at 11:00 PM, You will have to pay 2570") 
        if place == 2:
            print("Hi ",name, ", You are going to Mumbai ,at 09:00 AM,you will reach at 11:00 PM, You will have to pay 1150")
        if place == 3:
            print("Hi ",name, ", You are going to Chennai ,at 9:30 AM,you will reach at 11:00 PM, You will have to pay 1800")
        if place == 4:
            print("Hi ",name, ", You are going to Pune ,at 10:00 AM,you will reach at 11:00 PM, You will have to pay 1950")
        if place == 5:
            print("Hi ",name, ", You are going to Bangalore ,at 10:30 AM,you will reach at 11:00 PM, You will have to pay 3000") 
ticketsBought = int(input("How many tickets do you want?: "))
smartcardBalance = 15000            
for counter in range(1,ticketsBought+1):         
    ts= TravelSystem()
    b = input("what is your name: ")
    age = int(input("what is your age: "))
    print("""WELCOME TO TRAVEL SYSTEM
            press 1 to go To Delhi
            press 2 to go To Mumbai
            press 3 to go To Chennai
            press 4 to go To Pune
            press 5 to go To Bangalore""")
    a = int(input("Enter the Number: "))
    if age <= 5:
        print("you have bought a ticket for free")
    elif age > 5 and age <= 15:
        if a == 1:
            print(ts.printTicket(1,b))
            Bus.seatBlock
            print("""YOU CAN PAY IN TWO WAYS
                    press 1 to use smartcard
                    press 2 to use cash""")
            payment = int(input("please enter the way you want to pay: "))
            if payment == 1:
                print("you have gotten a discount of 50% as you are 15 or bellow(and above 5)")
                print("you have payed 1285 for going to delhi")
                smartcardBalance = smartcardBalance - 1285
                print("you have ",smartcardBalance," left in your smart card")
                print("CONGRATULATIONS!!!You have bought a ticket to Delhi")
            else:
                print("CONGRATULATIONS!!!You have bought a ticket to Delhi")

        if a == 2:
            print(ts.printTicket(2,b))
            Bus.seatBlock
            print("""YOU CAN PAY IN TWO WAYS
                    press 1 to use smartcard
                    press 2 to use cash""")
            payment = int(input("please enter the way you want to pay: "))
            if payment == 1:
                print("you have gotten a discount of 50% as you are 15 or bellow(and above 5)")
                print("you have payed 575 for going to mumbai")
                smartcardBalance = smartcardBalance - 575
                print("you have ",smartcardBalance," left in your smart card")
                print("CONGRATULATIONS!!!You have bought a ticket to Mumbai")
            else:
                print("CONGRATULATIONS!!!You have bought a ticket to Mumbai")

        if a == 3:
            print(ts.printTicket(3,b))
            Bus.seatBlock
            print("""YOU CAN PAY IN TWO WAYS
                    press 1 to use smartcard
                    press 2 to use cash""")
            payment = int(input("please enter the way you want to pay: "))
            if payment == 1:
                print("you have gotten a discount of 50% as you are 15 or bellow(and above 5)")
                print("you have payed 900 for going to chennai")
                smartcardBalance = smartcardBalance - 900
                print("you have ",smartcardBalance," left in your smart card")
                print("CONGRATULATIONS!!!You have bought a ticket to Chennai")
            else:
                print("CONGRATULATIONS!!!You have bought a ticket to Chennai")

        if a == 4: 
            print(ts.printTicket(4,b))
            Bus.seatBlock
            print("""YOU CAN PAY IN TWO WAYS
                    press 1 to use smartcard
                    press 2 to use cash""")
            payment = int(input("please enter the way you want to pay: "))
            if payment == 1:
                print("you have gotten a discount of 50% as you are 15 or bellow(and above 5)")
                print("you have payed 975 for going to Pune")
                smartcardBalance = smartcardBalance - 975
                print("you have ",smartcardBalance," left in your smart card")
                print("CONGRATULATIONS!!!You have bought a ticket to Pune")
            else:
                print("CONGRATULATIONS!!!You have bought a ticket to Pune")

        if a == 5: 
            print(ts.printTicket(5,b))
            Bus.seatBlock
            print("""YOU CAN PAY IN TWO WAYS
                    press 1 to use smartcard
                    press 2 to use cash""")
            payment = int(input("please enter the way you want to pay: "))
            if payment == 1:
                print("you have gotten a discount of 50% as you are 15 or bellow(and above 5)")
                print("you have payed 1500 for going to bangalore")
                smartcardBalance = smartcardBalance - 1500
                print("you have ",smartcardBalance," left in your smart card")
                print("CONGRATULATIONS!!!You have bought a ticket to Bangalore")
            else:
                print("CONGRATULATIONS!!!You have bought a ticket to Bangalore")
    else:        
        if a == 1:
            print(ts.printTicket(1,b))
            Bus.seatBlock
            print("""YOU CAN PAY IN TWO WAYS
                    press 1 to use smartcard
                    press 2 to use cash""")
            payment = int(input("please enter the way you want to pay: "))
            if payment == 1:
                print("you have payed 2570 for going to delhi")
                smartcardBalance = smartcardBalance - 2570
                print("you have ",smartcardBalance," left in your smart card")
                print("CONGRATULATIONS!!!You have bought a ticket to Delhi")
            else:
                print("CONGRATULATIONS!!!You have bought a ticket to Delhi")

        if a == 2:
            print(ts.printTicket(2,b))
            Bus.seatBlock
            print("""YOU CAN PAY IN TWO WAYS
                    press 1 to use smartcard
                    press 2 to use cash""")
            payment = int(input("please enter the way you want to pay: "))
            if payment == 1:
                print("you have payed 1150 for going to mumbai")
                smartcardBalance = smartcardBalance - 1150
                print("you have ",smartcardBalance," left in your smart card")
                print("CONGRATULATIONS!!!You have bought a ticket to Mumbai")
            else:
                print("CONGRATULATIONS!!!You have bought a ticket to Mumbai")

        if a == 3:
            print(ts.printTicket(3,b))
            Bus.seatBlock
            print("""YOU CAN PAY IN TWO WAYS
                    press 1 to use smartcard
                    press 2 to use cash""")
            payment = int(input("please enter the way you want to pay: "))
            if payment == 1:
                print("you have payed 1800 for going to chennai")
                smartcardBalance = smartcardBalance - 1800
                print("you have ",smartcardBalance," left in your smart card")
                print("CONGRATULATIONS!!!You have bought a ticket to Chennai")
            else:
                print("CONGRATULATIONS!!!You have bought a ticket to Chennai")

        if a == 4: 
            print(ts.printTicket(4,b))
            Bus.seatBlock
            print("""YOU CAN PAY IN TWO WAYS
                    press 1 to use smartcard
                    press 2 to use cash""")
            payment = int(input("please enter the way you want to pay: "))
            if payment == 1:
                print("you have payed 1950 for going to Pune")
                smartcardBalance = smartcardBalance - 1950
                print("you have ",smartcardBalance," left in your smart card")
                print("CONGRATULATIONS!!!You have bought a ticket to Pune")
            else:
                print("CONGRATULATIONS!!!You have bought a ticket to Pune")

        if a == 5: 
            print(ts.printTicket(5,b))
            Bus.seatBlock
            print("""YOU CAN PAY IN TWO WAYS
                    press 1 to use smartcard
                    press 2 to use cash""")
            payment = int(input("please enter the way you want to pay: "))
            if payment == 1:
                print("you have payed 3000 for going to bangalore")
                smartcardBalance = smartcardBalance - 3000
                print("you have ",smartcardBalance," left in your smart card")
                print("CONGRATULATIONS!!!You have bought a ticket to Bangalore")
            else:
                print("CONGRATULATIONS!!!You have bought a ticket to Bangalore")

if ticketsBought == 5:
    print("you have gotten an extra ticket")