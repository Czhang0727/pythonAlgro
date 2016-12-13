def b_search(arr,target):

    low = 0
    high = len(arr) - 1

    while high > low + 1:
        mid = ( low + high ) / 2
        if arr[mid] < target:
            low = mid
        elif arr[mid] > target:
            high = mid
        else:
            high = mid
    
    print arr[low],arr[high]

    if arr[low] == target:
        return low
    if arr[high] == target:
        return high

    return -1

arr = [1,2,3,4,4,4,4,4,4,5,6,7,8,9,10]
print b_search(arr,4)
