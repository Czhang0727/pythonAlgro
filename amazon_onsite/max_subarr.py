import sys
def max_subarr(arr):
    
    total = 0
    min_pre_sum = 0
    max_sub_total =  -sys.maxint - 1
    for num in arr:
        total += num
        if total - min_pre_sum > max_sub_total:
            max_sub_total = total - min_pre_sum

        
        if total > min_pre_sum:
            min_pre_sum = total
    return max_sub_total

data = [1,2,3,4,-2,-2,4,-1,3]

print max_subarr(data)