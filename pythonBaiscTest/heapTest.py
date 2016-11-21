# trying to play with heap in python

# adding some random number in here
from random import randint
import heapq

arr = []

for i in range(10):
    arr.append(randint(0,100))

print arr

# lets do a heap sort

heapq.heapify(arr)
print heapq.nlargest(3,arr)

print arr
