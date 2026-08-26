from typing import List
import heapq

# Time complexity -> O(nlog(n)), space compexity -> O(n)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = []
        for n in arr:
            dist = abs(n - x)
            distances.append((dist, n))

        heapq.heapify(distances)
        ans = []
        for i in range(k):
            dist, num = heapq.heappop(distances)
            ans.append(num)
        ans.sort()

        return ans


########################################################################################

# Time complexity -> O(nlog(n)), space compexity -> O(n)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = []
        for n in arr:
            dist = abs(n - x)
            distances.append((dist, n))

        distances.sort(key=lambda y: y[0])
        ans = []
        for i in range(k):
            ans.append(distances[i][1])

        return ans.sort()



sol = Solution()
print(sol.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))