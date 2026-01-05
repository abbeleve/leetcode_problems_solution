# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        save_head = head
        amount_of_nodes = 0
        while head:
            head = head.next
            amount_of_nodes += 1
        head = save_head
        k = k % amount_of_nodes
        for rotation_number in range(k):
            save_head = head
            prev_node = None
            while head.next:
                prev_node = head
                head = head.next
            prev_node.next = None
            head.next = save_head
            
        return head