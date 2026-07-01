class DequeNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.length = 0
        self.max_length = k
        self.front = None # we add elements here
        self.rear = None # end of deque

    def insertFront(self, value: int) -> bool:
        if self.front is None:
            new_node = DequeNode(value = value)
            self.front = new_node
            self.rear = new_node
            self.length += 1
            return True
        if self.isFull():
            return False
        new_node = DequeNode(value=value)
        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.rear is None:
            new_node = DequeNode(value=value)
            self.rear = new_node
            self.front = new_node
            self.length += 1
            return True
        if self.isFull():
            return False
        new_node = DequeNode(value=value)
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front.next is None:
            self.front = None
            self.rear = None
            self.length -= 1
            return True
        self.length -= 1
        self.front = self.front.next
        self.front.prev = None
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.rear.prev is None:
            self.front = None
            self.rear = None
            self.length -= 1
            return True
        self.rear = self.rear.prev
        self.rear.next = None
        self.length -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.value

    def isEmpty(self) -> bool:
        return self.length == 0        

    def isFull(self) -> bool:
        return self.length == self.max_length


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()