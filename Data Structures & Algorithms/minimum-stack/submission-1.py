class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, num: int):
        self.stack.append(num)
        if not self.minStack:
            self.minStack.append(num)
        else:
            if self.minStack[-1] >= num:
                self.minStack.append(num)

    
    def pop(self):
        stackNum = self.stack.pop()
        if stackNum == self.minStack[-1]:
            self.minStack.pop()
        
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
        
# minStack = new MinStack()
# minstack.push(1)