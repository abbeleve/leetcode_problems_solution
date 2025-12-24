# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        power = 0
        while l1 and l2:
            num += pow(10, power) * (l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next
            power += 1
            print(num, power)
        while l1:
            num += pow(10, power) * l1.val
            l1 = l1.next
            power += 1
        while l2:
            num += pow(10, power) * l2.val
            l2 = l2.next
            power += 1
        print(num)
        num = str(num)
        list_of_nodes = []
        for number_index in range(len(num) - 1, -1, -1):
            list_of_nodes.append(ListNode(int(num[number_index]), None))
        for node_index in range(len(list_of_nodes) - 1):
            list_of_nodes[node_index].next = list_of_nodes[node_index + 1]
        return list_of_nodes[0]
