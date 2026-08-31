from typing import List

# Time complexity -> O(log( n * m)), space compexity -> O(n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = self.search_potential_row(matrix, target)
        if row_index != -1:
            return self.binary_search_over_row(row_index, matrix, target)
        
        return False


    def search_potential_row(self, matrix, target):
        low = 0
        high = len(matrix) - 1 # no of rows
        while low <= high:
            mid = low + (high - low) // 2

            # Is the target between the first and last element of this row?
            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[0])-1]:
                return mid
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def binary_search_over_row(self, row_index, matrix, target):
        low = 0
        high = len(matrix[row_index]) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False



########################################################################################

# Time complexity -> O(m log n), space compexity -> O(n)
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         is_found = False
#         for row in matrix:
#             is_found = self.search(row, target)
#             if is_found:
#                 return True
#         return False

#     def search(self, row, target) -> bool:
#         l, r = 0, len(row) - 1

#         while l <= r:
#             mid = (l + r) // 2
#             if row[mid] == target:
#                 return True
#             elif row[mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1

#         return False






sol = Solution()
print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))