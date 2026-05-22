from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # list as the value

        for s in strs:
            cur = [0] * 26

            for c in s:
                cNum = ord(c) - ord("a")
                cur[cNum] += 1
            res[tuple(cur)].append(s)

        
        return list(res.values())