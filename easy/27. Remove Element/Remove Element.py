from typing import List


# Time complexity -> O(n), space compexity -> O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        c = 0
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
                c += 1

        return c

sol = Solution()
print(sol.removeElement(nums = [3,2,2,3], val = 3))
print(sol.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
# print(sol.removeElement(nums=[2], val=3))
# print(sol.removeElement(nums=[2,2,2], val=2))
print(sol.removeElement(nums=[2,2,3], val=2))