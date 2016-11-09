class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        
        dp = {
            0 : -1    
        }
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            
            if sum in dp:
                return [dp[sum]+1, i]
            else:
                dp[sum] = i
        