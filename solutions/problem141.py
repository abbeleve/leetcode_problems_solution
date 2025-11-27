# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        stack = []
        node = head
        while node.next != None:
            if node in stack:
                return True
            stack.append(node)
            node = node.next