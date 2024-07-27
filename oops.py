'''
for example
Railway form --->class[Blueprint]
harry filled the form---->now harry's form----object
sayan filled the form----->now sayan's form----object
karan filled the form-----> now karan's form-----object
'''

class Person:
    name = 'Sayan'
    occupation = 'data scientist'
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = 'Sakshar'
a.occupation = 'doctor'
# print(a.name, a.occupation)
a.info()
