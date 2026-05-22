class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store the last appearance of asci char to it scorr5esponding posiition 
        # sliding window update if l is wihtin the valid window

        asci_char = [-1] * 128
        max_window = 0
        l = 0
        for r in range(len(s)):
            if asci_char[ord(s[r])] >= l:
                l = asci_char[ord(s[r])] + 1

            asci_char[ord(s[r])] = r
            max_window = max(max_window, r - l + 1)
        return max_window   

         