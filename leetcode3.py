def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    str1 = str(x)
    l1 = list(str1)
    l2 =[]
    l3 = []
    # for i in l1:
    #     a = int(i)
    #     l2.append(a)


    if len(l1)>1:
        i = 0

        while i < len(l1):


            if l1[i] == l1[-(i+1)]:
                print(l1[i])
                print(l1[-(i+1)])
                print("appending")
                l3.append(1)
            else:
                # print("number is not palindrome")
                l3.append(0)




            i = i+1
    else:
        return False
    print(l3)
    c = l3.count(0)
    if c != 0:
        return False
    else:
        return True

print(isPalindrome(0))