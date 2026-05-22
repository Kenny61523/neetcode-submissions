class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
            return ""
        
        count_t = {}
        window = {}
        
        # Count frequency of characters in t
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        l = 0
        have = 0
        need = len(count_t)  # Number of unique characters in t
        res = [-1, -1]
        resLen = float("infinity")
        
        # Expand the window with the right pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # Check if current character satisfies frequency requirement
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            # Shrink the window from the left as much as possible
            while have == need:
                # Update the result if this window is smaller
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                # Remove the leftmost character from the window
                window[s[l]] -= 1 
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1 

        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""