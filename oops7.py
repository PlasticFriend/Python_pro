'''
del keyword -used to delet object properties
 and the object itself
'''
class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("sayan")
print(s1.name)
# del s1
print(s1)

'''
private attributes and methods
this are meant to be used only inside the class and not outside the class
'''
class Account:
    def __init__(self, acc_no, acc_pass,):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def resetPass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
# print(acc1.acc_pass)

# we should not allow account password to print as it may be sensitive so we should make it private for this add __ before the argument

acc1.resetPass() # -- as this methodis inside class then it can print the password

