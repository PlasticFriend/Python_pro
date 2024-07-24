l = [3,5,9,1,2,7,8,6]
print(l)
print(type(l))
a = l[0]
print(a)
#lins item index are similar to string index
# append method to add items

# l.append(11)
print(l)
#list can contain different data types
# can also use len method
print(len(l))
# can use in conditions like this
if 3 in l:
    print("yes")
else:
    print("no")

# to print all elements of a list
print(l)
print(l[0:])
# --jump index
print(l[::2])
#generating list on the fly
lst = [i for i in range(4)]
lst2 = [i*i for i in range(8)]
lst3 = [i*i for i in range(10) if i%2 ==0]
print(lst)
print(lst2)
print(lst3)