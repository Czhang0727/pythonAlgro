# trying to play with heap in python

# adding some random number in here
from random import randint
import heapq

class Node:

    def __init__(self, val):
        self.value = val

    def __cmp__(self, obj):
        return -cmp(self.value, obj.value)



arr = []

for i in range(10):
    arr.append(randint(0,100))
print arr

maxHeap = []

for num in arr:
    data = Node(num)
    heapq.heappush(maxHeap,data)

print '[',
for d in maxHeap:
    print d.value,
# lets do a heap sort
print ']'
heapq.heapify(arr)

print heapq.heappop(maxHeap).value
print arr
