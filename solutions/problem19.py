# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return None
        prev_head = None
        next_head = None
        save_head = head
        max_index = 0
        while head:
            head = head.next
            max_index += 1
        head = save_head
        index = 1
        n = max_index - n + 1
        while head:
            if index == n - 1:
                prev_head = head
            if index == n + 1:
                next_head = head
                break
            head = head.next
            index += 1

        if prev_head is None:
            save_head = next_head
            return save_head
        if next_head is None:
            prev_head.next = None
            return save_head
        prev_head.next = next_head
        return save_head