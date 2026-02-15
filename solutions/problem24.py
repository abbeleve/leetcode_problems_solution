# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        save_head = head.next
        last_head = None
        while head is not None:
            if head.next is not None:
                if last_head:
                    last_head.next = head.next
                next_head = head.next
                head.next = next_head.next
                next_head.next = head
                last_head = head
            else:
                if last_head:
                    last_head.next = head
            head = head.next
            
        return save_head