def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    l = s.split()
    lst = l[(len(l)-1)]
    lstr = list(lst)
    return len(lstr)
print(lengthOfLastWord("hello world"))