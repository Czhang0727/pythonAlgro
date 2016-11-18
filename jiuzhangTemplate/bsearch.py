def binary_search(arr, target):
    arr.sort();
    begin = 0;
    end = len(arr);
    while(begin + 1 < end):
        mid = begin + (end - begin) / 2;
        if(target < arr[mid]):
            end = mid;
        elif (target > arr[mid]):
            begin = mid;
        else:
            end = mid;
    if arr[end] == target:
        return end;
    if arr[begin] == target:
        return begin;
    return -1;
    
arr = [1,2,3,4,5,6,7,8,9]
print binary_search(arr,1);