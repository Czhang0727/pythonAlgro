def sqrt(val):
    
    low = 1
    high = val


    while low + 1 < high:
        mid = (low + high)/2
        if mid * mid > val:
            high = mid
        else:
            low = mid
    if high * high < val:
        return high
    return low

print sqrt(1000)


def cpy(arr1):
    if len(arr1) == 0:
        return []
    res = []
    res.append(arr1[0])
    res += cpy(arr1[1:])
    return res

arr1 = [1,2,4,4,6,3,2,7]
print cpy(arr1)