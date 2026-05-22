class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        maxF = 0 
        res = 0
        l = 0

        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            maxF = max(maxF, cnt[s[r]])

            while (r - l + 1) - maxF > k:
                cnt[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res

