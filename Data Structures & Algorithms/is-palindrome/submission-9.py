class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1

        while l <= r:
            while (not 97 <= ord(s[l].lower()) <= 122) and (not 48 <= ord(s[l].lower()) <= 57) and l < r:
                l += 1
            
            while (not 97 <= ord(s[r].lower()) <= 122) and (not 48 <= ord(s[l].lower()) <= 57) and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        
        return True
