class Player:
    def __init__(self, firstName, lastName, position, jerseyNo, club):
        self.first = firstName
        self.last = lastName
        self.position = position
        self.jerseyNo = jerseyNo
        self.club = club
    def greeting(self):
        return 'Hi, I am {} {} and I play the role of {}'.format(self.first, self.last, self.position)
Ronaldo = Player("Cristiano","Ronaldo", 'left wing',7, 'Real Madrid')
print(Ronaldo.greeting())