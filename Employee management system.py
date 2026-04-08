#inheritance = one class gets properties and methods from another
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.balance = balance
    def display(self):
        return f"{self.name}, {self.balance}"
class Manager(Employee):
    def __init__(self, name, salary, team_Size):
        super.__init__(name, salary) #super is used to call the parent method/constructor
        self.team_size = team_size
class Developer(Employee):#method overriding same method name, different behaviour
    def display(self):
        print(f" Developer: {self.name}, Salary: {self.salary}")
        
        Employee = [                   #polymorphism(same method, different behaviour)
    Manager("Hema", 50000, 5),
    Developer("pavana", 40000)
]


