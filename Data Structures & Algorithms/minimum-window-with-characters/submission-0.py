class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
            return ""
        
        count_t = {}
        window_count = {}
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        l = 0
        formed = 0
        required = len(count_t)
        min_length = float("inf")
        res = ""
        
        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in count_t and window_count[char] == count_t[char]:
                formed += 1
            
            while formed == required:
                # Update result if this window is smaller
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    res = s[l:r+1]
                
                # Remove the leftmost character
                window_count[s[l]] -= 1
                if s[l] in count_t and window_count[s[l]] < count_t[s[l]]:
                    formed -= 1
                l += 1
        
        return res