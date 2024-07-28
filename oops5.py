'''
static methods---these methods dont use self parameter

'''
class Student:
    @staticmethod  # decorater
    def college():
        print('ABC college')


s1 = Student()
s1.college()