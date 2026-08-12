"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        return self.recurse((0, 0), (len(grid), len(grid)))

    def recurse(self, left_up: tuple, right_down: tuple):
        node = Node(None, None, None, None, None, None)
        only_element = self.grid[left_up[0]][left_up[1]]
        flag = True
        for i in range(left_up[0], right_down[0]):
            for j in range(left_up[1], right_down[1]):
                if self.grid[i][j] != only_element:
                    flag = False
                    break
            if not(flag):
                break
        if flag:
            node.val = only_element
            node.isLeaf = True
        else:
            node.val = 1
            node.isLeaf = False
            mid_r = (left_up[0] + right_down[0]) // 2
            mid_c = (left_up[1] + right_down[1]) // 2
            
            node.topLeft = self.recurse(
                (left_up[0], left_up[1]), 
                (mid_r, mid_c)
            )
            node.topRight = self.recurse(
                (left_up[0], mid_c), 
                (mid_r, right_down[1])
            )
            node.bottomLeft = self.recurse(
                (mid_r, left_up[1]), 
                (right_down[0], mid_c)
            )
            node.bottomRight = self.recurse(
                (mid_r, mid_c), 
                (right_down[0], right_down[1])
            )
        return node