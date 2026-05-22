from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l  = 0
        substring = set()
        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[i])
            res = max(res, i - l + 1)
        
        return res
            
