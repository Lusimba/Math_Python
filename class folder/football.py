class Player():
    def __init__(self,firstName,lastName,position,number,club):
        self.firstName = firstName
        self.lastName = lastName
        self.position = position
        self.number = number
        self.club = club
    def greating(self):
        return "I am {} {} I am a {} My jersey number is {} I play for {}".format(self.firstName,self.lastName,\
        self.position,self.number,self.club)
player_1 = Player("D.de","Gea","goalkeeper",1,"Manchester United")
player_2 = Player("A","Young","defender",18,"Manchester United")
player_3 = Player("V","lindelof","defender",2,"Manchester United")
player_4 = Player("P","Jones","defender",4,"Manchester United")
player_5 = Player("D","dalot","defender",20,"Manchester United")
player_6 = Player("A","Herrera","RM",21,"Manchester United")
player_7 = Player("N","matić","CM",31,"Manchester United")
player_8 = Player("P","Pogba","LM",6,"Manchester United")
player_9 = Player("J","lingard","RW",14,"Manchester United")
player_10 = Player("M","Rashford","CF",10,"Manchester United")
player_11 = Player("A","Martial","LW",11,"Manchester United")
print(player_1.greating())
print("            -                  ")
print(player_2.greating())
print("            -                  ")
print(player_3.greating())
print("            -                  ")
print(player_4.greating())
print("            -                  ")
print(player_5.greating())
print("            -                  ")
print(player_6.greating())
print("            -                  ")
print(player_7.greating())
print("            -                  ")
print(player_8.greating())
print("            -                  ")
print(player_9.greating())
print("            -                  ")
print(player_10.greating())
print("            -                  ")
print(player_11.greating())
print("            -                  ")