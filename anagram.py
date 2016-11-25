def anagram(s,t):
    map1 = [0] * 256
    for c in s:
        map1[ord(c)] += 1
    
    for c in t:
        map1[ord(c)] -= 1

    for count in range(256):
        if(map1[count] != 0):
            return False
    return True

#wrong answer
def anagram2(s,t):
    flag1 = 0
    flag2 = 0
    for c in s:
        flag1 = flag1 ^ ord(c)
    print flag1

    for c in t:
        flag2 = flag2 ^ ord(c)
    print flag2
    return flag1 == flag2

print anagram2("az", "by")