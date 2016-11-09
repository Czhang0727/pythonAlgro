class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        curPos = 0
        newArrPos = 0
        removedCount = 0
        while curPos != len(A):
            if A[curPos] == elem:
                removedCount += 1
            else:
                A[newArrPos] = A[curPos]
                newArrPos+=1
            curPos+=1
        A = A[0:len(A) - removedCount] 
        print A


sol = Solution()
A = [0,4,4,0,4,4,4,0,2]
sol.removeElement(A, 4)
print A