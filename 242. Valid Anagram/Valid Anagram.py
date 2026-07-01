
# Time complexity -> O(nlog(n)), space compexity -> O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        ls, lt = 0, 0
        while ls < len(s):
            if s[ls] != t[lt]:
                return False
            ls += 1
            lt += 1

        return True
    

####################################################################

# Time complexity -> O(n), space compexity -> O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(0, len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return False
        
        return True



s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))