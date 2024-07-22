# this a demontration of a faulty calculater
a  = int(input("enter the first digit: "))
b  = int(input("enter the second digit: "))
oper = input("enter your operater: ")
if oper== "+":
    result = a*b
    print(result)
elif oper== "-":
    result = a+b
    print(result)
elif oper== "*":
    result = a-b
    print(result)
else:
    print("please enter a valid operator")