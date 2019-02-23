sender = 10000
reciever = 10000
class Transfer():
    def __init__(self, transfer_amount, acc_no):
        self.transfer_amount = transfer_amount
        self.acc_no = acc_no
    def showBalance(self,transfer_amount):
        return "you are left with ",sender - transfer_amount," money in your account"          
    def send(self,transfer_amount,acc_no):
        senderName = "person"
        senderAccount = 500032
        receiverName = "anotherperson"
        recieverAccount = 500031
        return "\n Name:{} \n account no.:{} \n you are sending: {}".format(receiverName,recieverAccount,transfer_amount) 
        if acc_no == recieverAccount:
            return "\n Name:{} \n account no.:{} \n you are sending: {}".format(receiverName,recieverAccount,transfer_amount) 
    
x = input("Please enter the account number:  ")
y = int(input("how much do you want to send: "))
tr = Transfer(x,y)
tr.send(x,y)



