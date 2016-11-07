def bfs(S, currentRes, result, currentPos):
    result.append(currentRes)
    for pos in range(currentPos, len(S)-1):
        currentRes.append(S[pos])
        bfs(S,currentRes, result, pos)
        currentRes.pop()
        

def subsets(S):
    # write your code here
    res = []
    currentRes = []
    bfs(S, currentRes, res, 0)
    return res

print subsets([1,2,3])