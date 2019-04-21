class Employee:
    raise_amount = 1.04
    def __init__(self, firstName, lastName, salary):
        self.first = firstName
        self.last = lastName
        self.pay = salary
    def fullName(self):
        return ('{} {}' .format(self.first, self.last))
    def currentSalary(self):
        self.pay = int(self.pay*self.raise_amount)
        return self.pay
#subclass of Employee superclass
class Developer(Employee):
    raise_amount=1.10
    def __init__(self, firstName, lastName, salary, prog_lang):
        super().__init__(firstName, lastName, salary)
        self.prog_lang = prog_lang
    def details(self):
        return('\nName: {} {} \n salary: {} \n Proficiency: {}'.format(self.first, self.last, self.pay, self.prog_lang))
#subclass of Employee
class Manager(Employee):
    def __init__(self, firstName, lastName, salary, employees = None):
        super().__init__(firstName, lastName, salary)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

emp=Employee('Neville', 'Lusimba', 50000)
#We can raise the salary of an individual by applying a percentage increment
emp1 = Developer('Brian', 'Sim', 90000, 'Python')
print (emp1.currentSalary())