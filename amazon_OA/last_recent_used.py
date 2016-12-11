class LRU_cache:

    class d_link_list_node:
        
        def __init__(self, val):
            self.value = val
            self.pre = None
            self.next = None
    

    # this is node -1
    
    def __init__(self):
        self.cache = self.d_link_list_node(0)
        self.hash_map = {}
    
    def print_list (self):
        pointer = self.cache

        while pointer is not None:
            print pointer.value,"->",
            pointer = pointer.next
        print "None"

    def get_val(self, key):
        # check element in hash_map (see if the element in cache)
        tmp = self.hash_map.get(key)
        
        if tmp is not None:
            # element exist
            tmp.pre.next = tmp.next
            if tmp.next is not None:
                tmp.next.pre = tmp.pre
            tmp.next = self.cache.next
            tmp.pre = self.cache
            self.cache.next.pre = tmp
            self.cache.next = tmp
            return tmp.value
        else:
            # woops, we dont have the element
            self.print_list()
            return -1


    def set_val(self, key, val):
        tmp = self.hash_map.get(key)
        
        if tmp is not None:
            tmp.value = val
            tmp.pre.next = tmp.next
            if tmp.next is not None:
                tmp.next.pre = tmp.pre
            tmp.next = self.cache.next
            tmp.pre = self.cache
            self.cache.next.pre = tmp
            self.cache.next = tmp
        else:
            # create new node, append at front, 
            # add to hash_map

            new_node = self.d_link_list_node(val)

            new_node.next = self.cache.next
            new_node.pre = self.cache
            if new_node.next is not None:
                new_node.next.pre = new_node 
            self.cache.next = new_node
            self.hash_map[key] = new_node
        self.print_list()

lru = LRU_cache()
lru.set_val(0,"CHENYI")
lru.set_val(1,"JIBEI")
print lru.get_val(0)
lru.set_val(2,"BOB")
print lru.get_val(2)
lru.set_val(3,"DREAM")
lru.set_val(2,"HAHA")
print lru.get_val(3)
print lru.get_val(5)


