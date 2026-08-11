from typing import List


# Time complexity -> O(n*m), space compexity -> O(n*m)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])

        ans = []
        for c in range(col):
            s = []
            for r in range(row):
                s.append(matrix[r][c])
            ans.append(s)

        return ans


sol = Solution()
print(sol.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
# print(sol.transpose(matrix = [[1,2,3],[4,5,6]]))