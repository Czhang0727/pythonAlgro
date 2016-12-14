def word_break(s,dic):

    dp = [False] * (len(s) + 1)
    dp[0] = True

    for index in xrange(len(s) + 1):
        for trace_index in range(index,-1,-1):
            if dp[trace_index]:
                if s[trace_index : index] in dic:
                    dp[index] = True
                    break
    return dp[-1]


s = "abcd"
dic = ["a","abc","b","cd"]

print word_break(s,dic)