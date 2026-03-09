# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        save_head = head
        node_counter = 0
        node_list = []
        while head:
            node_counter += 1
            node_list.append(head)
            head = head.next
        head = save_head
        
        for i in range(len(node_list) // 2):
            left_node, right_node = node_list[i], node_list[node_counter - i - 1]
            next_left_node = left_node.next
            left_node.next = right_node
            if i == node_counter // 2 - 1:
                if node_counter % 2 == 0:
                    right_node.next = None
                else:
                    right_node.next = node_list[node_counter // 2]
                    node_list[node_counter // 2].next = None
                break
            right_node.next = next_left_node
            
        return save_head