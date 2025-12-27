# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        if left == right:
            return head
        save_head = head
        index = 1
        prev_left_node = None
        next_right_node = None

        while head:
            if index == left - 1:
                prev_left_node = head
            if index == right - 1:
                prev_right_node = head
                right_node = head.next
                next_right_node = head.next.next
            if index == left:
                left_node = head
                next_left_node = head.next
            if index == right:
                right_node = head
            index += 1
            head = head.next

        if left + 1 == right:
            if prev_left_node:
                prev_left_node.next = right_node
            right_node.next = left_node
            if next_right_node:
                left_node.next = next_right_node
            return save_head

        if prev_left_node:
            prev_left_node.next = right_node
        right_node.next = next_left_node
        prev_right_node.next = left_node
        if next_right_node:
            left_node.next = next_right_node
        return save_head