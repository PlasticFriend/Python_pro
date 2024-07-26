
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    for i in range(len(l1)):
        l1.insert(i, l1.pop())
    for i in range(len(l2)):
        l2.insert(i, l2.pop())
    comb1 = int(''.join(map(str, l1)))
    comb2 = int(''.join(map(str, l2)))
    comb3 = comb1+comb2
    r_list = [int(digit) for digit in str(comb3)]

    for i in range(len(r_list)):
        r_list.insert(i, r_list.pop())

    return r_list
l1 = [2,4,3]
l2 = [5,6,4]
a= addTwoNumbers(l1, l2)
print(a)

