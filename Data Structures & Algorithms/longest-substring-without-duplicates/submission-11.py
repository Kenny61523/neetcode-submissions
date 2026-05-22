class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window 
        # keep track of the largest window - res
        # keep track of the largest current window 
        # create -1 array of size 128 
        
        # iterate through the array with i pointer. l to i is the window 
        # storage of acii numbers - size 128 chars update the asci position with i. 
        
        # use the position of char in s to keep track of the window.j 
        
        # return max(arrary)
        # edge case 

        max_window = 0
        l = 0
        acsi_arr = [-1] * 128
        for i in range(len(s)):
            char_ascii = ord(s[i])

            # if char is seen agian AND the last appearance is inside our window
            if acsi_arr[char_ascii] >= l:
                l = acsi_arr[char_ascii] + 1
            
            acsi_arr[char_ascii] = i

            max_window = max(max_window, i - l + 1)
        
        return max_window

            