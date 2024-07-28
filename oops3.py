'''
Attributes
two types of attributes
1. Class attributes----same for all the objects in the class
2. object/instance attributes-----defined by self.<attribute>
3.object attribute>class attribute


'''

class Person:
    college = "ABC college"
    name = 'anonymous'

    def __init__(self,n,o): # --- parameterised constructer
        self.name = n
        self.occ = o
        self.college
    def __init__(self):  # ---Defalut constructer
        print("hey i am a person")


a = Person()
print(a.college)

