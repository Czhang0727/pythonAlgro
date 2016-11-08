class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        # write your code here
        nag_flag = False
        INT_MAX = 2147483647
        INT_MIN = -2147483648
    
        str = str.strip()
        
        if len(str) == 0:
            return 0
            
        if(str[0] == '-'):
            nag_flag = True
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        res = 0
        
        # cut until first non-number char appears
        count = 0
        for c in str:
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                count+=1
            else: 
                break
        str = str[:count]
        for c in str:
            res *= 10
            res += ord(c) - ord('0')
            
        res = res * (-1 if nag_flag else 1)
        
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        
        return res
        
            
        