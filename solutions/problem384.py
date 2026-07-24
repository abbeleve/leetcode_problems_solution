import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled_nums = []
        indexes = [i for i in range(len(self.nums))]
        while indexes:
            ran = random.randint(0, len(indexes) - 1)
            random_index = indexes[ran]
            shuffled_nums.append(self.nums[random_index])
            indexes.pop(ran)
        return shuffled_nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()