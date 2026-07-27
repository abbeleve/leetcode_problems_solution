# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        save_head = head
        max_k = right - left
        first, last, prev_last = None, None, None
        counter = 1
        while counter < left:
            if counter == left - 1:
                first = head
            head = head.next
            counter += 1
            
        def recurse(head, k):
            nonlocal first, last, prev_last
            if k == max_k:
                last = head.next
                prev_last = head
                return head
            node = recurse(head.next, k + 1)
            node.next = head
            return head
        
        head = recurse(head, 0)
        head.next = last
        if first is not None:
            first.next = prev_last
            return save_head
        return prev_last