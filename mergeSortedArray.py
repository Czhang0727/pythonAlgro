class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        posB = n-1;
        posA = m-1;
        newPos = m + n -1
        while(posA >= 0 and posB >= 0):
            if A[posA] > B[posB]:
                A[newPos] = A[posA]
                posA-=1
            else:
                A[newPos] = B[posB]
                posB-=1
            newPos -= 1
            
        
        restPos = 0
        restArr = []
        if posA >= 0:
            restPos = posA
            restArr = A
        else:
            restPos = posB
            restArr = B
            

        print restArr
        print restPos
        while restPos >= 0:
            A[newPos] = restArr[restPos]
            restPos-=1
            newPos-=1        
        return A
        
sol = Solution()
print sol.mergeSortedArray([9,10,11,12,13,0,0,0,0], 5, [4,5,6,7], 4)
