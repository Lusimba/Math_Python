Balance = 10000
class Transfer:
    def __init__(self, user_input, receiverNo, amount):
        self.acc=user_input
        self.receiver=receiverNo
        self.transamount=amount
    def transfer(self):
        try:
            user_input=int(input('Please enter your account number'))
            acc_no=[123, 234, 456, 567, 789, 890]
            customers =['x', 'y', 'z', 'a', 's', 'b']
            #print(acc_no.index(user_input))
            y=acc_no.index(user_input)
            print('Hi {}, your account number is {}'.format(customers[y], user_input))
        except:
            print('Sorry, your account number does not exist')