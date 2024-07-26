def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) != 0:
        wrd1 = strs[0]
        wrd2 = strs[1]
        wrd3 = strs[2]

        str = ''
        l_S = [len(wrd1), len(wrd2), len(wrd3)]
        min_len = min(l_S)
        i = min_len
        while i >= 0:

            if wrd1[:i] == wrd2[:i]:

                if wrd1[:i] == wrd3[:i]:
                    str = str + wrd1[:i]
                    break
            i = i - 1

        return str
    else:
        return ''
lp = [""]
print(longestCommonPrefix(lp))