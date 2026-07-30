# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        core_head = None
        def recurse(head):
            if head.next is None:
                nonlocal core_head
                core_head = head
                return head
            next_head = recurse(head.next)
            next_head.next = head
            return head
        recurse(head)
        head.next = None
        return core_head