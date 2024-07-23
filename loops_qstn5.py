#program to calculate factorial using for loop
a = int(input("enter the number: "))
facto=1
for i in range(1,a+1):
    facto = facto*i
print(facto)