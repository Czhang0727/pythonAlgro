arr = []
def get(pos):
    return arr[pos]

def sortInBigArr(target):

    begin = 0
    end = 1

    while get(end) != -1:
        end **2;

    mid = 0
    while begin + 1 < end:
        mid = (begin + end)>>1

        if get(mid) == -1:
            end = mid
        else:
            if get(mid) > target:
                end = mid
            elif get(mid) < target:
                begin = mid
            else:
                return mid
    
    if get(begin) == target:
        return begin
    if get(end) == target:
        return end
    return -1
