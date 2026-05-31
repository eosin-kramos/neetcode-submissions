class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {
            ']': '[',
            '}' : '{',
            ')' : '('
        }

        for char in s:
            if char in bracket:
                if stack and bracket[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False

