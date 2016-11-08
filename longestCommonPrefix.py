class trie:
    
    def __init__(self, str):
        self.head = {}
        cur = self.head
        for c in str:
            # create a new node with val c
            cur[c] = {}
            cur = cur[c]
        
    # this function will return depth of last node it inserted
    def insert_tree(self, str):
        depth = 0
        cur = self.head
        for c in str:
            if(c in cur):
                cur = cur[c]
                depth += 1
            else:
                break
        return depth
            
            
        
        # traversal tree
        
        
        return depth

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    
    # data structure will looks like this
    '''
    node = {
        'A' : {nodes}
    }
    '''
    def longestCommonPrefix(self, strs):
        # write your code here
        #build a try tree
        if(len(strs) == 0):
            return ""
        
        tree = trie(strs[0])
        maxLen = sys.maxint
        
        for str in strs[1:]:
            # for each string, we need to try a insert, then return depth
            # of common prefix
            common_prefix_len = tree.insert_tree(str)
            if maxLen > common_prefix_len:
                maxLen = common_prefix_len
        return strs[0][:maxLen]