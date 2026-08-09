from typing import List

# Time complexity -> O(nlog(n)), space compexity -> O(n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.merge_sort(arr=nums, left=0, right=n-1)

        return nums


    def merge_sort(self, arr: List[int], left: int, right: int):
        if left < right:
            mid = (left + right) // 2

            self.merge_sort(arr=arr, left=left, right=mid)
            self.merge_sort(arr=arr, left=mid+1, right=right)
            self.merge(arr=arr, left=left, mid=mid, right=right)

    def merge(self, arr: List[int], left: int, mid: int, right: int):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[left+i]
        for j in range(n2):
            R[j] = arr[mid+1+j]

        i = 0
        j = 0
        k = left
        while i < n1 and j < n2:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1


nums = [5,1,1,2,0,0]
sol = Solution()
print(sol.sortArray(nums))