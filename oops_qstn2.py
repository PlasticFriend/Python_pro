'''
create account class with 2 attributes - balance&account nuber
create methods for debit, credit & printing the balance.
'''


class Account:
    # bal = 0
    def __init__(self,acc,bal):
        self.acc = acc
        self.bal = bal
    def credit(self, amount):
        self.bal = self.bal+amount
    def debit(self, amount):
        self.bal = self.bal + amount










