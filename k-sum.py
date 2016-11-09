class Solution:
    # need sort before we process
    def k_sum(self, k, target, arr, begin_index):
        res = []
        # end case K = 0
        if k == 0 :
            if target == 0:
                res.append([])
            return res
        
        for i in range(begin_index, len(arr) - k + 1 ):
            if (i > begin_index) and (arr[i] == arr[i - 1]) :
                continue
            
            # go through next level
            for subArr in self.k_sum(k-1, target - arr[i], arr, i + 1):
                subArr.append(arr[i])
                res.append(subArr)
        return res
            

sol = Solution()
A = [-1, 0, 1, 2, -1, -4]
A.sort()
print sol.k_sum(3,0,A,0)

