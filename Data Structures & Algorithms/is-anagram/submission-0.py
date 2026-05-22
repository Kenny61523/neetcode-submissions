class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}

        for charS in s:
            dictS[ord(charS)] = dictS.get(ord(charS), 0) + 1

        for charT in t:
            dictT[ord(charT)] = dictT.get(ord(charT), 0) + 1
        
        return dictS == dictT
