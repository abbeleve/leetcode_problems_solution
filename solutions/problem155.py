class MinStack:

    def __init__(self):
        self.minimal_elements = [10**4]
        self.stack = []

    def push(self, val: int) -> None:
        if self.minimal_elements[-1] > val:
            self.minimal_elements.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        deleted_elem = self.stack.pop()
        if deleted_elem == self.minimal_elements[-1]:
            self.minimal_elements.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimal_elements[-1]
    
s = MinStack()
print(s.push(-2), s.push(0), s.push(-3), s.getMin())