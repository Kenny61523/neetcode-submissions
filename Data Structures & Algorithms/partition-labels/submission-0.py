class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # greedy 
        charToEnd = {}

        for i, c in enumerate(s):
            # { char: lastIndex }
            charToEnd[c] = i
        
        print(charToEnd)
        size = 1
        end = 0
        res = []

        for i, c in enumerate(s):
            # check the lastIndex of chars in the current substring
            if end < charToEnd[c]:
                end = charToEnd[c]
            
            if i == end:
                res.append(size)
                size = 0
            size += 1
            
        return res