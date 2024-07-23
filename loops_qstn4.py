# find the sum of n natural numbers
a = int(input("enther the number: "))
# sum  = (a*(a+1))/2  --------this is a one line solution but i will try using loops
summ=0
for i in range (1,a+1):
    summ = summ+i

print(summ)