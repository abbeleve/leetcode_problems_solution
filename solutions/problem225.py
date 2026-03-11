class MyStack:

    def __init__(self):
        self.list = []
        self.size = -1

    def push(self, x: int) -> None:
        self.list.append(x)
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.list.pop()

    def top(self) -> int:
        return self.list[self.size]

    def empty(self) -> bool:
        return self.size == -1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()