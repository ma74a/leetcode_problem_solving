from typing import List


# Time complexity -> O(n), space compexity -> O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k: # check if the window is bigger than k
                hs.remove(nums[l]) # if, then remove the most left item
                l += 1
            if nums[r] in hs:
                return True
            hs.add(nums[r])
        return False

    

# nums = [1,2,3,1]
nums = [1,2,3,1,2,3]
k = 2
# k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))