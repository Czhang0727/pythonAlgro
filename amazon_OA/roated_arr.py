class roated_arr:

    def __init__(self, size):
        self.data = [0 for x in xrange(size + 1)]

    def updates(self, update_info):
        self.data[update_info[0]] += update_info[2]
        self.data[update_info[1] + 1] -= update_info[2]


    def inquery(self):
        res = []
        res_sum = 0

        for val in self.data:
            res_sum += val
            res.append(res_sum)
        res.pop()
        return res

my_arr = roated_arr(5)
updates = [
   [1,  3,  2],
   [2,  4,  3],
   [0,  2, -2]]

for inq in updates:
    my_arr.updates(inq)
    print my_arr.inquery()
