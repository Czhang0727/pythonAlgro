
def compareStrings(A, B):
    # write your code here
    mapData = [0] * 26
    baseNum = ord('A')
    for c in A:
        mapData[ord(c) - baseNum] += 1
    
    print mapData
    for c in B: 
        mapData[ord(c) - baseNum] -= 1
        if mapData[ord(c) - baseNum] < 0:
            return False
    print mapData
    return True
# fail because python took number as value not ref
def compareStrings2(A, B):
    # write your code here
    mapData = [0] * 26
    baseNum = ord('A')
    for c in A:
        mapData[ord(c) - baseNum] += 1
    
    print mapData
    for c in B:
        curChar = mapData[ord(c) - baseNum] 
        curChar -= 1
        if curChar < 0:
            return False
    print mapData
    return True

print compareStrings("ABCDEFG", "ACC")