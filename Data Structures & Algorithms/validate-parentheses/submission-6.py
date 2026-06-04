class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}' : '{',
                    ']' : '[',
                    ')' : '('}
        
        stack = []

        for sym in s:
            if sym not in brackets:
                stack.append(sym)
            else:
                if len(stack) >= 1:
                    openSym = stack.pop()
                else:
                    return False
                if openSym != brackets[sym]:
                    return False
        
        if len(stack) >= 1:
            return False
        return True