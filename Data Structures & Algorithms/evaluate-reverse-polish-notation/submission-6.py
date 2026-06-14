class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : a - b,
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : a / b
        }

        numStack = []

        for token in tokens:
            if token in operators:
                numB = numStack.pop()
                numA = numStack.pop()
                value = operators[token](int(numA), int(numB))
                numStack.append(value)
            else:
                numStack.append(token)
        
        return int(numStack.pop())