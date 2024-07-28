'''
create a class that takes name and marks of 3 subjects as arguments in constructer,
then create a method to rint the average marks.
'''
class Student:
    def __init__(self,name,n1,n2,n3):
        self.name = name
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def get_avg(self):
        avg = (self.n1+self.n2+self.n3)/3
        print(f"{self.name} your average marks is {avg}")

sayan = Student('sayan',85,89, 93)
sayan.get_avg()