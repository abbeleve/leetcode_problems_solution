# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        self.nodes = []
        save_head = head
        while head is not None:
            self.nodes.append(head)
            head = head.next
        head = save_head
        self.mergeSort(0, len(self.nodes))
        for i in range(len(self.nodes) - 1):
            self.nodes[i].next = self.nodes[i + 1]
        self.nodes[len(self.nodes) - 1].next = None
        return self.nodes[0]

    def mergeSort(self, l, r):
        if r - l == 0:
            return
        if r - l == 2:
            if self.nodes[l].val > self.nodes[r - 1].val:
                save = self.nodes[l]
                self.nodes[l] = self.nodes[r - 1]
                self.nodes[r - 1] = save
                return
        if r - l == 1:
            return
        m = (l + r) // 2
        self.mergeSort(l, m)
        self.mergeSort(m, r)

        result = []
        i, j = l, m
        while i < m and j < r:
            if self.nodes[i].val < self.nodes[j].val:
                result.append(self.nodes[i])
                i += 1
            else:
                result.append(self.nodes[j])
                j += 1
        
        while i < m:
            result.append(self.nodes[i])
            i += 1
        
        while j < r:
            result.append(self.nodes[j])
            j += 1
        
        for i in range(len(result)):
            self.nodes[i + l] = result[i]