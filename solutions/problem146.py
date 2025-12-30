class LinkedList:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.amount_of_keys = 0
        self.hash_table = {}
        self.head = LinkedList(None, None)
        self.pointer = self.head

    def get(self, key: int) -> int:
        if key in self.hash_table:
            inner_pointer = self.head
            prev_pointer = None
            while inner_pointer:
                if inner_pointer.val == key:
                    if prev_pointer is not None:
                        prev_pointer.next = inner_pointer.next
                        self.pointer.next = inner_pointer
                        self.pointer = self.pointer.next
                    else:
                        self.head = self.head.next
                        inner_pointer.next = None
                        self.pointer.next = inner_pointer
                        self.pointer = self.pointer.next
                    break
                prev_pointer = inner_pointer
                inner_pointer = inner_pointer.next
            return self.hash_table[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash_table and self.amount_of_keys == self.capacity:
            self.hash_table[key] = value
            LRU_value = self.hash_table.pop(self.head.val)
            self.head = self.head.next
            self.pointer.next = LinkedList(val=key, next=None)
            self.pointer = self.pointer.next
            return LRU_value
        if self.amount_of_keys == 0:
            self.head.val = key
            self.amount_of_keys += 1
            self.hash_table[key] = value
        if key not in self.hash_table:
            self.pointer.next = LinkedList(val=key, next=None)
            self.pointer = self.pointer.next
            self.amount_of_keys += 1
            self.hash_table[key] = value
        if key in self.hash_table:
            self.hash_table[key] = value

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
obj.put(2, 1)
# obj.put(2, 2)
print(obj.get(2))
obj.put(3, 2)
# print(obj.get(1))