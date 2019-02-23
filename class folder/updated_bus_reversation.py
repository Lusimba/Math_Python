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
