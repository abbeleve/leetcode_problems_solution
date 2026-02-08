# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        save_head = head
        head_next = head.next
        hash_duplicates = {}
        while head_next is not None:
            if head.val == head_next.val:
                head_next = head_next.next
                hash_duplicates[head.val] = True
            else:
                head = head_next
                head_next = head_next.next
        head.next = None
        
        return save_head