
data = [[2,3],[9,15],[3,4],[6,7], [1,14]]


def sort_arr(val1,val2):

    return 1 if val1[0] > val2[0] else -1

def merge_inverval(data):
    if len(data) == 0:
        return []

    data.sort(cmp=sort_arr)
    cur = data[0]
    data.pop(0)
    size = len(data)
    for index in xrange(size):
        if cur[1] < data[0][0]:
            data.append(cur)
            cur = data[0]
            data.pop(0)
        else:
            cur[1] = max(data[0][1],cur[1])
            data.pop(0)
    data.append(cur)
    return data

print merge_inverval(data)