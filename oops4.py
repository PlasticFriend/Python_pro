'''
methods
In class two things can be stored 1. data 2. methods
methods are function inside classs
'''
class Student:
    college_name = 'ABC college'

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def hello(self):
        print("welcome,", self.name)

    def get_marks(self):
        print(f"{self.name}")


s1 = Student('karan', 97)
s1.hello()
s1.get_marks()