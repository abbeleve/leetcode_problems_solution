# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        start_node = ListNode(None, head)
        end_node = ListNode(None, None)
        save_head = head
        while head.next is not None:
            head = head.next
        head.next = end_node
        head = save_head

        hash_map = {}
        while head is not None:
            hash_map[head.val] = hash_map.get(head.val, 0) + 1
            head = head.next
        head = save_head

        keys = list(hash_map.keys())
        list_for_deletion = set()
        for key in keys:
            if hash_map[key] > 1:
                list_for_deletion.add(key)
        
        save_head = None
        left_node, middle_node, right_node = start_node, head, head.next
        while right_node is not None:
            if middle_node.val in list_for_deletion:
                left_node.next = right_node
                middle_node = middle_node.next
                right_node = right_node.next
            else:
                if save_head is None:
                    save_head = middle_node
                left_node = left_node.next
                middle_node = middle_node.next
                right_node = right_node.next
        left_node.next = None
        return save_head