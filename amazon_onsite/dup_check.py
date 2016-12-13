def find_dup(arr):
    tmp = 0

    for i in arr:
        tmp = tmp ^ i
    print tmp

data = [1,1,1,1,2,2,2,3,3,4,4,5,5]

find_dup(data)