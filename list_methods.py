# append method
l = [1,2,4,5,6,7,8]
print(l)
l.append(9)
print(l)
#sort method--------arranges in assending or descending order
l.sort()
print(l)
#for descending order use reverse=true
l.sort(reverse=True)
print(l)
#------reverse ----reverse the original list
l1 =[2,4,6,78,8]
l1.reverse()
print(l1)
# ---index method----this method returns the index of the first occurance of the given
print(l1.index(6))
# count method---------count the given item
print(l1.count(2))
# insert method to inset at a given index-----insert
l1.insert(1,99)
print(l1)
# ----extend method
l.extend(l1)
print(l)
# can also add list like
l2 = l+l1