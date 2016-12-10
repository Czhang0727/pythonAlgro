
# implement a union find set

class union_find():
    

    self.father = []

    def __init__(self, arr):
        self.arr = arr
        self.father = [ 0 for i in range(len(arr) + 1)]
        
    def find(self, val):

        if father[x] == 0:
            return x 
        father[x] = find(father[x])
        return father[x]

    def union(self, a,b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            father[root_a] = root_b