from typing import List


# Time complexity -> O(n)^2, space compexity O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            for u in range(i+1, len(nums)):
                if nums[i] + nums[u] == target:
                    res.append(i)
                    res.append(u)
                    return res
                
        return


###########################################################################################

# Time complexity -> O(n), space compexity O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} # value -> index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hm:
                return [hm[diff], i]
            hm[nums[i]] = i

nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))