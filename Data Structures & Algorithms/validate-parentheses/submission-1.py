class Solution:
    def isValid(self, s: str) -> bool:
        #create bool to represent each bracket type
        stack = []
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            #case when closed c is closed paraenthesis
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # case c is open parenthesis
            else:
                stack.append(c)
        
        return True if not stack else False 
                
