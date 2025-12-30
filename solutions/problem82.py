# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def remove(self, head: Optional[ListNode], head_prev: Optional[ListNode]) -> Optional[ListNode]:
        if head_prev is None:
            return head.next
        if head.next:
            head_prev.next = head.next
            return head_prev.next
        return None
        
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        save_head = head
        head_prev = None
        head_anch = None
        amount_of_duplicates = 0
        while head:
            if head.val == head_prev.val:
                amount_of_duplicates += 1
                head = head.next
                continue
            else:
                if head_prev is None:
                    head_prev = head
                    head = head.next
                    continue
                head_prev.next = head
                head_prev = head
                head = head.next
                
        return save_head