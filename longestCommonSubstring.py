class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def getSubStr(self, str):
        result = []
        sub = ""
        
        for i in range(len(str)):
            for j in range(i,len(str)):
                result.append(str[i:j+1])
        # print result
        return result
        
    def longestCommonSubstring(self, A, B):
        # write your code here
        Aarr = self.getSubStr(A)
        Barr = self.getSubStr(B)
        
        max_len = 0
        for s in Barr:
            if (s in Aarr) and (len(s) > max_len):
                max_len = len(s)
                print s

        print ".com code" in Aarr
        return max_len

class SolutionDP:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        
        # mark up dp mathod
        dp = [[0 for x in range(len(A))] for y in range(len(B))]
        maxCount = 0
        for x in range(len(A)):
            for y in range(len(B)):
                
                if(A[x] == B[y]):
                    if x == 0 or y == 0:
                        dp[y][x] = 1
                    else:
                        data = dp[y-1][x-1] + 1
                        dp[y][x] = data
                    # check maxCount
                    if maxCount < dp[y][x]:
                            maxCount = dp[y][x]
        # print dp
      
        return maxCount
                

sl = SolutionDP()
print sl.longestCommonSubstring("www.lintcode.com code", "www.ninechapter.com code")