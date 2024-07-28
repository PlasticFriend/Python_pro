'''
4 pillars of oops- 1. abstraction 2. encapsulation 3. inheritance 4. polymorphism
Abstraction- hiding the implementation details of a class and only show the user important features

'''


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started")


car1 = Car()
car1.start()



