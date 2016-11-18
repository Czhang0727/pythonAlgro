class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here

        arr = n.split(".")
        left = 0
        right = 0
        
        try:
            left = int(arr[0])
            right = float("0." + arr[1])
        except ValueError:
            return "ERROR"
        
        # get left part
        res =  str("{0:b}".format(left))
        
        # get right part
        
        # since we have one bit for [.]
        bits = 32 - len(res)
        base = 1.0

        if right == 0:
            res
            return res
        else:
            rightBits = ""
            print bits
            for i in range (16):
                base /= 2
                if right >= base:
                    right -= base
                    rightBits += "1"
                else:
                    rightBits += "0"
                if right == 0:
                    break
                # print base," ",right," ",rightBits
        
        print right
        if right == 0:
            return res  + "." + rightBits
        else:
            return "ERROR"
            

sol = Solution()
print sol.binaryRepresentation("17817287.6418609619140625")