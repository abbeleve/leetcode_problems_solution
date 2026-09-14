import random

class Solution:

    def __init__(self, w: list[int]):
        self.indexes = 0
        for weight in w:
            self.indexes += weight
        self.w = []
        for weight in w:
            if len(self.w) == 0:
                self.w.append(weight)
            else:
                self.w.append(self.w[-1] + weight)

    def binary_search(self, target):
        arr = self.w
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def pickIndex(self) -> int:
        random_index = random.randint(1, self.indexes)
        res = self.binary_search(random_index)
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()