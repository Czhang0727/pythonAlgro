def bfs(S, currentRes, result, currentPos):
    # print "current:",currentRes
    if (len(currentRes) > 0): 
        tmp = list(currentRes)
        result.append(tmp)
    for pos in range(currentPos, len(S)):
        currentRes.append(S[pos])
        bfs(S,currentRes, result, pos + 1)
        currentRes.pop()
    # print "result:",result
    return result
        

def subsets(S):
    # write your code here
        res = []
        currentRes = []
        bfs(S, currentRes, res, 0)
        return res


print subsets([0])