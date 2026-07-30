from typing import List

# Time complexity -> O(n), space compexity -> O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = []

        for i in range(n - 1, -1, -1):
            print(f"out: {stk}")
            while len(stk) > 0 and temperatures[i] >= temperatures[stk[-1]]:
                print(f"in: {stk}")
                stk.pop()
            if len(stk) > 0:
                ans[i] = stk[-1] - i

            stk.append(i)

        return ans
        



temperatures = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(temperatures=temperatures))