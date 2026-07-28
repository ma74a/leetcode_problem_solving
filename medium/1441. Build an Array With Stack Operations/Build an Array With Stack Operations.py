from typing import List

# Time complexity -> O(n), space compexity -> O(1)
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0
        for n in range(1, n+1):
            if i == len(target):
                break

            ans.append("Push")

            if n == target[i]:
                i += 1
            else:
                ans.append("Pop")

        return ans


###########################################################################################

# Time complexity -> O(n*m), space compexity -> O(m)
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        stack = []
        for i in range(1, n+1):
            if stack == target:
                break
            if i in target:
                stack.append(i)
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
        print(stack)
        return ans

sol = Solution()
print(sol.buildArray(target = [1,2,3], n = 3))
print(sol.buildArray(target = [1,3], n = 3))
# print(sol.buildArray(target = [1,2], n = 4))