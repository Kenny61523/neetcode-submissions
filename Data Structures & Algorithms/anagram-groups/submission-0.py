class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
  
        res = defaultdict(list) #constructs a dictionary with values of type list
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
            
        return list(res.values())




