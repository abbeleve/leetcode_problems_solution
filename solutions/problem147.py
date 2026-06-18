# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev_head = ListNode(val = -32000, next = head)
        saved_head = prev_head
        sorted_part = head
        while sorted_part.next is not None:
            if sorted_part.next.val >= sorted_part.val:
                sorted_part = sorted_part.next
            else:
                prev_head = saved_head
                while sorted_part.next.val > prev_head.next.val:
                    prev_head = prev_head.next
                current = sorted_part.next
                sorted_part.next = current.next
                current.next = prev_head.next
                prev_head.next = current
        return saved_head.next