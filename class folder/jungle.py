class Jungle:
    def __init__(self, name, vore, place, behavior, pred, prey):   
        self.animal = name
        self.vores = vore
        self.live = place
        self.behave = behavior
        self.predator = pred
        self.prey = prey
    def Name(self):
        print("\n Name: {} \n type: {} \n Position: {} \n Speciality: {} \n Prey: {} \n Predator: {}" .format(self.animal, self.vores, self.live, self.behave, self.prey, self.predator))
class Animal(Jungle):
    def __init__(self, name, vore, place, behavior, pred, prey):
        super().__init__(name, vore, place, behavior, pred, prey)
    def details(self):
        print("\n Name: {} \n type: {} \n Position: {} \n Speciality: {} \n Prey: {} \n Predator: {}" .format(self.animal, self.vores, self.live, self.behave, self.prey, self.predator))
printer_1 = Jungle('Worm', 'Herbivore', '3rd', 'Slow walker', 'Sparrow', 'Hawk')
printer_2 = Animal('Sparrow', 'Insectivore', '2nd', 'Fast digger', 'Hawk', 'Worm' )
printer_3 = Animal('Hawk', 'Carnivores', '1st', 'Super sight', 'Worms', 'Sparrow')
printer_1.Name()
printer_2.details()
printer_3.details()