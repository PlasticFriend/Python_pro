'''
Attributes
two types of attributes
1. Class attributes----same for all the objects in the class
2. object/instance attributes-----defined by self.<attribute>
3.


'''

class Person:
    college = "ABC college"
    def __init__(self,n,o): # --- parameterised constructer
        self.name = n
        self.occ = o
    def __init__(self):  # ---Defalut constructer
        print("hey i am a person")


a = Person()
print(a.college)

