#see the last two lines

senc =[2233, 2323, 3223, 2332, 3232, 3322]
senn =['Advaith.Y', 'Advaith.B', 'Daiwik', 'Tanishq', 'Vidit', 'Ganesh']
recc =[4455, 4545, 5445, 4554, 5454, 5544]
recn =['Advaith.Y', 'Advaith.B', 'Daiwik', 'Tanishq', 'Vidit', 'Ganesh']
bal = 1000

class Trans:
    def __init__(self, tran, sencar, reccar):
        self.trs = tran
        self.a_1 = sencar
        self.a_2 = reccar
        try:
            self.senca = senc.index(sencar)
            self.senna = senn[self.senca]
            self.recca = recc.index(reccar)
            self.recna = recn[self.recca]

        except Exception as ex:
            print("Sorry,", ex)

    def transact(self):
        if(self.trs < bal):
            print("You sent $%s to %s" %(self.trs, self.recna))
            print("Your name is %s and account number is **** and place is %s" %(self.senna, self.senca+1))
        else:
            print("Enna daa rascala! Emiti raa dunnepothu!")

acc_1 = int(input("What is your account number           "))
acc_2 = int(input("What's the reciever's account number  "))
acc_3 = int(input("How much money do you want to send    "))

trans_1 = Trans(acc_3, acc_1, acc_2)
trans_1.transact()
#Done
#Copy the whole thing
number =int(input("what is your account number :"))
list1=[ 123,456,789,1012,1013,1014,1015]
list2=["rudolph","touro","ringo","shindo","butto","MYBUTT","MY NAME IS JEFF"]
print(list1.index(number))
y = list1.index(number)
print("Hi {} ,your account number is {} ".format(list2[y],number))