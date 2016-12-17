# Round 1 question 1
# a robot can move 1,2 or 3 steps determine how much steps we need to go to not

def ways_of_moving(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    dp = [0] * (n + 1)
    dp [0:4] = [0,1,2,4]
    for i in xrange(4,n + 1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    # print dp
    return dp[-1]
# test

print ways_of_moving(5)

# question 2
# implement LRU

class d_linked_list_node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class last_recent_used:
    def __init__(self, max_size):
        self.head = d_linked_list_node(0)
        self.tail = d_linked_list_node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data_map = {}
        self.max_size = max_size
        self.current_size = 0

    def get(self, key):
        tmp = self.data_map.get(key)
        if tmp is None:
            return None
        tmp.prev.next = tmp.next
        tmp.next.prev = tmp.prev
        tmp.next = self.head.next
        self.head.next.prev = tmp
        tmp.prev = self.head
        self.head.next = tmp
        return tmp.val


    def put(self, key, val):
        tmp = self.data_map.get(key)
        if tmp is not None:
            tmp.val = val
            self.get(key)
            return
        if self.current_size == self.max_size:
            tmp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None

        new_node = d_linked_list_node(val)
        
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next = new_node
        new_node.next.prev = new_node

# Round 2 question 1
# give a visitor list [5,7,9,2,11] represent which level that visitor want to go

class min_stack_node:
    def __init__(self, val):
        self.val = val

    def __cmp__(self,b):
        return self.val - b.val

class max_stack_node:
    def __init__(self, val):
        self.val = val
    def __cmp__(self,b):
        return b.val - self.val

def min_clam(visitors, N):

    import heapq
    # record bigger Value
    min_stack = []
    # record smaller value
    max_stack = []
    min_sum = 0
    cur_sum = 0

    for val in visitors:
        heapq.heappush(min_stack, min_stack_node(val))
        cur_sum += val - 1 
    min_sum = cur_sum

    for index in xrange(1,N):
        cur_sum -= len(min_stack)
        cur_sum += len(max_stack)
        if index == min_stack[0].val:
            heapq.heappop(min_stack)
            heapq.heappush(max_stack, max_stack_node(index))
        if cur_sum < min_sum:
            min_sum = cur_sum

        if len(max_stack) == 0:
            break
    return min_sum


# Round 4 question 1 implement a candidate_manage system
# functions : get, add, delete, get_first_10
# similar to LRU
class candidate_manage:
    # double list + hashmap
    pass
