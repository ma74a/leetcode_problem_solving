from typing import List

# Time complexity -> O(nlog(n)), space compexity -> O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            if n not in hm:
                hm[n] = 1
            else:
                hm[n] += 1

        # reversed_d = {v: k for k, v in hm.items()}
        
        freq = []
        for num, count in hm.items():
            freq.append((count, num))

        freq.sort(reverse=True)


        ans = []
        for i in range(k):
            ans.append(freq[i][1])
        
        return ans
        


nums = [1,1,1,2,2,3]
k = 2
# nums=[3,0,1,0]
# k = 1
sol = Solution()
print(sol.topKFrequent(nums, k))