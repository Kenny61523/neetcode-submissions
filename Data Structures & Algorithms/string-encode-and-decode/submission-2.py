class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "あ"
        return res

    def decode(self, s: str) -> List[str]:
        list = []
        str = ""

        for c in s:
            if c == "あ":
                list.append(str)
                str = ""
            else: str += c
            
        return list
            

        
