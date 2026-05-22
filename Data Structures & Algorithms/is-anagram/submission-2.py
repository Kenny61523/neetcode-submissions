class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dictS = {}
        dictT = {}

        for c in s:
            dictS[ord(c)] = dictS.get(ord(c), 0) + 1
            
        for c in t:
            dictT[ord(c)] = dictT.get(ord(c), 0) + 1

        return dictS == dictT