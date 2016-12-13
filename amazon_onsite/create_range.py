class range:

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __str__(self):
        return "[" + str(self.begin) + "," + str(self.end) + "]"

def create_range_arr(arr):
    arr.sort()
    res = []
    res.append(range(arr[0], arr[0]))
    for index, num in enumerate(arr):
        if index == 0:
            continue
        if num == res[-1].end + 1:
            res[-1].end += 1
        else:
            res.append(range(num,num))
    return res
    


data = [2,3,4,6,7,8,9,12,13,14,26,27,29]
print "[",
for val in create_range_arr(data):
    print val,
print "]"
