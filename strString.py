def strStr(source, target):
    # write your code here
    # travel through source
    for s_len in range(len(source)):
        print source[s_len:s_len + len(target)]
        if target == source[s_len:len(target)]:
            return s_len
    # traval through all string, nothing found
    return -1

print strStr("abcdef","bc")