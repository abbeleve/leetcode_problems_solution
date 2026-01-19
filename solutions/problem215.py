import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = heapq.heapify([-i for i in nums])
        if k == 1:
            return -heap[0]
        queue = [heap[0]]
        index = 0
        max_counter = 1 
        result = []
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node)
            for i in range(index, len(result)):
                left = 2 * i + 1
                right = 2 * i + 2
                queue.append()