import time
list1=[ 123,456,789,1012,1013,1014,1015]
list2=["rudolph","touro","ringo","shindo","butto","MYBUTT","MY NAME IS JEFF"]
list3=[ 234,567,8910,1112,1314,1516,1718]
list4=["idiot","myface","myfoot","tata","yourface","IDC","MY NAME IS ADVAITH"]
balance=100000
class Ding:
    def __init__(self,number,amount,receiver):
         self.number= number
         self.amount=amount
         self.receiver=receiver
    def transfer(self):
        accPosition = list1.index(self.receiver)
        accName = list2[accPosition]
        print("you are sending",amount ,"to" ,accName )
        print("okay continue")
        print("sending")
        time.sleep(1)
        print("almost sent")
        time.sleep(1)
        print("how much more time??????")
        time.sleep(1)
        print("I hate my job!!!!!")
        time.sleep(1)
        print("at last ,you have sent the money")
        new_balance= balance-amount
        print ( "your account  currently has ",new_balance)       
number =int(input("what is your account number :"))
if number in list3 :
    amount =int(input("what is the amount your sending :"))
    if amount < balance and amount > 0:
        receiver =int(input("who are you sending your dirty filthy money toooooooooo :"))   
        if receiver in list1:
            di = Ding(number,amount,receiver)
            print(di.transfer())
        else:
            print("wrong account number")
    else:
        print("enter valid amount")         
else:
    print("wrong account number")

