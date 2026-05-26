# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        save_head = head
        self.length = 0
        while head is not None:
            self.length += 1
            head = head.next
        self.head = save_head

    def getRandom(self) -> int:
        random_int = random.randint(0, self.length - 1)
        save_head = self.head
        while random_int > 0:
            save_head = save_head.next
            random_int -= 1
        return save_head.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()