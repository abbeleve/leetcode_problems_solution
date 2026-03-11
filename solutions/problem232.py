class Node:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyQueue:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        node = Node(val=x)
        if self.size == 0:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        print(self.tail.val)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return None
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val

    def peek(self) -> int:
        if self.empty():
            return None
        return self.head.val

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()