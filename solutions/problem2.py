# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str_n1 = ''
        str_n2 = ''
        node = l1
        while True:
            str_n1 = str(node.val) + str_n1
            node = node.next
            if node.next == None:
                str_n1 = str(node.val) + str_n1
                break
        
        node = l2
        while True:
            str_n2 = str(node.val) + str_n2
            node = node.next
            if node.next == None:
                str_n2 = str(node.val) + str_n2
                break

        return [int(i) for i in str(int(str_n1) + int(str_n2))]