class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"]" : "[", "}" : "{", ")" : "("}
        openP = []
        if s == []: return True
        if len(s) % 2 == 1: return False

        for i, p in enumerate(s):
            if p in ['[', '{', '(']:
                openP.append(p)
            
            #empty case => False
            elif not openP:
                return False

            elif not openToClose[p] == openP[-1]:
                return False
            
            else:
                openP.pop()

        return len(openP) == 0
