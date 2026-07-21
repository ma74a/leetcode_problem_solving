from typing import List

# Time complexity -> O(klog(k) . n), space compexity -> O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)

        return list(anagrams.values())
    

strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]
sol = Solution()
print(sol.groupAnagrams(strs))