"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        head_saved = head
        index = 0
        while head:
            head.index = index
            head = head.next
            index += 1
        stack_of_nodes = []
        index = 0
        head = head_saved
        while head:
            node = Node(head.val, None, None)
            if head.random:
                node.random_index = head.random.index
            else:
                node.random_index = None
            stack_of_nodes.append(node)
            head = head.next
        for i, node in enumerate(stack_of_nodes):
            if i < len(stack_of_nodes) - 1:
                node.next = stack_of_nodes[i + 1]
            if node.random_index is not None:
                node.random = stack_of_nodes[node.random_index]
        return stack_of_nodes[0]