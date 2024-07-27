'''
constructer function
this is invoked when a object is created like in example a,b

'''
class Person:
    def __init__(self,n,o):
        print("hey i am a person")
        self.name = n
        self.occ = o

    def info(self):
        return(f"{self.name} is a {self.occ}")


a = Person("Sayan", "student")
b = Person("sakshar", "doctor")
# print(a.info())
# b.name = 'Sakshar'
# b.occ = 'doctor'
print(a.info())
print(b.info())