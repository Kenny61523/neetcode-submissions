class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0
        count1 = {}
        count2 = {}
        
        # Initialize frequency counts for s1
        for char in s1:
            count1[char] = count1.get(char, 0) + 1
        
        # Initialize frequency counts for the first window of s2
        for i in range(len(s1)):
            count2[s2[i]] = count2.get(s2[i], 0) + 1
        
        # Sliding window over s2
        for r in range(len(s1), len(s2)):
            if count1 == count2:
                return True
            # Add the new character to the window
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            # Remove the leftmost character from the window
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            l += 1
        
        # Check the final window
        return count1 == count2