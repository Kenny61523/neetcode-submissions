from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sudo code
        res = defaultdict(list) # value
        cur = [0] * 26
        
        for s in strs: 
            cur = [0] * 26
            for c in s: 
                cur[ord(c) - ord('a')] += 1
            # if tuple(cur) in res: 
            res[tuple(cur)].append(s)

        print(list(res.values()))
        return list(res.values())
            