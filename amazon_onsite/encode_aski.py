def encdoe_ask(s):
    res = ""
    s = s.lower()
    for c in s:
        c = ord(c) - ord('a') + 1
        res += (str(c))
    return res

def decode_ask(s):
    res = []

    while len(s) > 0:
        val1_1 = chr(int(s[0]) + ord("a") - 1)
        val1_2 = ""
        val2 = ""
        if len(s) >= 2 and int(s[:2]) <= 26:
            val2 = chr(int(s[:2]) + ord("a") - 1)
            val1_2 = chr(int(s[1]) + ord("a") - 1)
            if len(res) == 0:
                res.append(val2)
                res.append(val1_1 + val1_2)
            else:
                size = len(res)
                for index in xrange(size):
                    res.append(res[index] + val1_1 + val1_2)
                    res[index] += val2
       
        if val2 != "":
            s = s[2:]
        else:
            s = s[1:]
            if len(res) == 0:
                res.append(val1_1)
            else:
                for index,data in enumerate(res):
                    print "v1"
                    res[index] = data + val1_1
    return res

print encdoe_ask("aB")
print decode_ask("1282123")


