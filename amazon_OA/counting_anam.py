def counting_anam(s,needle):

    diff = {}
    result = []

    for c in needle:
        if c in diff:
            diff[c] += 1
        else:
            diff[c] = 1

    for c in s[:len(needle)]:
        if c in diff:
            diff[c] -= 1
            if diff[c] == 0:
                diff.pop(c,None)
        else:
            diff[c] = -1

    for i in xrange(len(needle), len(s)):
        # print diff
        # print s
        if len(diff) == 0:
            result.append(i-len(needle))
        
        # next statement
        if s[i] in diff:
            diff[s[i]] -= 1
            if diff[s[i]] == 0:
                diff.pop(s[i],None)
        else:
            diff[s[i]] = -1

        if s[i - len(needle)] in diff:
            diff[s[i-len(needle)]] += 1
            if diff[s[i-len(needle)]] == 0:
                diff.pop(s[i - len(needle)], None)
        else:
            diff[s[i - len(needle)]] = 1

    return result

        
    
print counting_anam("cbcaebabacd","abc")
