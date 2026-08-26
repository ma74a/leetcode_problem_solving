from typing import List
import math


# Time complexity -> O(nlog(n)), space compexity -> O(n)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        origin_point = (0, 0)
        for point in points:
            dist = self.measuare_distance(origin_point, point)
            distances.append((dist, point))

        # print(distances)
        distances.sort(key=lambda x:x[0])
        ans = []
        for i in range(k):
            ans.append(distances[i][1])
        # print(ans)

        return ans
        
    def measuare_distance(sel, origin, point):
        return math.sqrt((point[0] - origin[0]) ** 2 + (point[1] - origin[1]) ** 2)



sol = Solution()
print(sol.kClosest(points = [[1,3],[-2,2]], k = 1))