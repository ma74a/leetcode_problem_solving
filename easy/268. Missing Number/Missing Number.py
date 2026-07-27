from typing import List

# Time complexity -> O(n), space compexity -> O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = (1 + len(nums)) * len(nums) // 2
        for n in nums:
            sum -= n

        return sum