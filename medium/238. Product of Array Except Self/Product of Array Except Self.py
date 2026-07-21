from typing import List

# Time complexity -> O(n), space compexity -> O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix = [1] * n
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]


        ans = [1] * n
        for i in range(0, n):
            ans[i] = prefix[i] * suffix[i]

        return ans
        
        



# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
sol = Solution()
print(sol.productExceptSelf(nums))