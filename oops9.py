class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name =name
        # to call constructer of parent class use super method
        super().start()

car1 = ToyotaCar("Pirus","electric")
print(car1.type)
