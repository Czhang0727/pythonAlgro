def count_char(s):

    count = 0
    cur = ''
    cur = s[0]
    res = ""
    for c in s:
        if cur == c:
            count += 1
        else:
            res += (("" if count == 1 else str(count)) + cur)
            cur = c
            count = 1
            print res
    res += (("" if count == 1 else str(count)) + cur)
    return res

s = "AABBCDDD"
print count_char(s)
        
