from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        first = strs[0]
        
        # Iterate through each character position
        for i in range(len(first)):
            char = first[i]
            # Check if all strings have this character and it matches
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return first[:i]
        
        return first




# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["flower","flower","flower","flower"]
sol = Solution()
print(sol.longestCommonPrefix(strs))
