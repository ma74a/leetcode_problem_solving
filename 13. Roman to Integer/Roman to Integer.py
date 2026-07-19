
# Time complexity -> O(n), space compexity -> O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        r_to_i = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = len(s)
        ans = 0
        i = 0
        while i < n -1:
            if r_to_i[s[i]] < r_to_i[s[i+1]]:
                ans += r_to_i[s[i+1]] - r_to_i[s[i]]
                i += 2
            else:
                ans += r_to_i[s[i]]
                i += 1
        if i != n:
            ans += r_to_i[s[i]]

        return ans



# s = "III"
# s = "LVIII"
s = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(s))