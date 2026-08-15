from typing import List


# Time complexity -> O(n*m), space compexity -> O(n*m)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n * m != r * c:
            return mat

        # result = [[0] * c for _ in range(r)]
        flat = []
        for row in mat:
            for val in row:
                flat.append(val)

        reshaped = []
        for i in range(r):
            row = []
            for u in range(c):
                row.append(flat[i*c+u])
            reshaped.append(row)
        

        return reshaped


sol = Solution()
print(sol.matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))

"""
[
    [1,2],
    [3,4]
]
[
    [1, 2, 3, 4]
]
"""