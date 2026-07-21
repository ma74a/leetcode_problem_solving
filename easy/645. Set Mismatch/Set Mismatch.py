from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sum_all = 0
        for i in range(1, len(nums) + 1):
            sum_all += i
        hm = {}
        for n in nums:
            if n not in hm:
                hm[n] = 1
            else:
                hm[n] += 1
        
        ans = []
        for k, v in hm.items():
            if v > 1:
                ans.append(k)
        
        for k in hm.keys():
            sum_all -= k
        
        ans.append(sum_all)
        
        return ans

        

# nums = [1,2,2,4]
# nums = [1,1]
nums = [2,2]
sol = Solution()
print(sol.findErrorNums(nums))
