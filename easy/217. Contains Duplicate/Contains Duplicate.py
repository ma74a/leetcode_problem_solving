from typing import List
from collections import Counter


# Time complexity -> O(n), space compexity -> O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = Counter(nums)
        for key, value in hm.items():
            if value > 1:
                return True
        return False


########################################################################

# Time complexity -> O(nlog(n)), space compexity -> O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
##########################################################################

# Time complexity -> O(n), space compexity -> O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for i in range(0, len(nums)):
            if nums[i] in hs:
                return True
            hs.add(nums[i])
        return False

nums = [1,2,3,1]
sol = Solution()
print(sol.containsDuplicate(nums))