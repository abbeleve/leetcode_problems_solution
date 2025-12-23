# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resulting_node = None
        head_node = None
        while list1 and list2:
            if list1.val < list2.val:
                if resulting_node is None:
                    resulting_node = ListNode(list1.val)
                    head_node = resulting_node
                else:
                    resulting_node.next = ListNode(list1.val)
                    resulting_node = resulting_node.next
                list1 = list1.next
            else:
                if resulting_node is None:
                    resulting_node = ListNode(list2.val)
                    head_node = resulting_node
                else:
                    resulting_node.next = ListNode(list2.val)
                    resulting_node = resulting_node.next
                list2 = list2.next
        
        while list1:
            if resulting_node is None:
                    resulting_node = ListNode(list1.val)
                    head_node = resulting_node
            else:
                resulting_node.next = ListNode(list1.val)
                resulting_node = resulting_node.next
            list1 = list1.next

        while list2:
            if resulting_node is None:
                    resulting_node = ListNode(list2.val)
                    head_node = resulting_node
            else:
                resulting_node.next = ListNode(list2.val)
                resulting_node = resulting_node.next
            list2 = list2.next
            
        return head_node