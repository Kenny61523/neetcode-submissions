from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store the last appearance of asci char to it scorr5esponding posiition 
        # sliding window update if l is wihtin the valid window
        
        q = deque()
        max_window = 0
        l = 0
        for r in range(len(s)):
            while s[r] in q:
                l += 1
                q.popleft()

            q.append(s[r])
            max_window = max(max_window, r - l + 1)
        return max_window   

         