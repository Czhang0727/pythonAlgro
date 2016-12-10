def merge_two_array(arr1, arr2):
    res = []

    while len(arr1) > 0 and len(arr2) > 0:

        if arr1[0] > arr2[0]:
            res.append(arr2[0])
            arr2.pop(0)
        else:
            res.append(arr1[0])
            arr1.pop(0)

    
    if len(arr1) > 0:
        while len(arr1) > 0:
            res.append(arr1[0])
            arr1.pop(0)
    else:
        while len(arr2) > 0:
            res.append(arr2[0])
            arr2.pop(0)
    return res

print merge_two_array([1,2,3],[2,5])
