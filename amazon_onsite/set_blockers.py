# input n get 
# n = 3
# return 112233 -> 312132 

result = []
def bfs(arr, res_set ,n):
    if len(arr) == 0:
        result.append(list(res_set))
        return res_set
    for index,num in enumerate(arr):
        
        if len(res_set) > 0 and (num - index - 1) >= 0 and (res_set[num - index - 1] != num):
            continue
        res_set.append(num)
        bfs(arr[:index] + arr[index+1:], res_set, n)
        res_set.pop()
        
def set_blockers(n):
    possible_val = []
    for i in xrange(n):
        possible_val  += [i + 1,i + 1]
    bfs(possible_val,[],n)
    return result

# print validate([3, 1, 2, 1, 3, 2],set([1,2,3]))
# print set_blockers(3)
for row in set_blockers(3):
    print row