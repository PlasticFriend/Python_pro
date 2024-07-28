'''
Inheritance
when one calss derives the properties and methods of another class (parent)

'''

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.brand)
print(car1.start())
print(car1.color)


'''
inheritance is of three types
1.single inheritance----single parent class and a single derived class from that.
2.multi level inheritance----base to derives and then to another derived class.
3.multiple level inheritance----a derived class can inherit properties of different classes
'''


class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type
                                # -----Examlpe of multilevel inheritance
car3  = Fortuner("disel")
car3.start()



