import random

class Solution:

    def __init__(self, nums: list[int]):
        self.hash_map = {}
        for index, num in enumerate(nums):
            if num in self.hash_map:
                self.hash_map[num].append(index)
            else:
                self.hash_map[num] = [index]

    def pick(self, target: int) -> int:
        return self.hash_map[target][random.randint(0, len(self.hash_map[target]) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)