class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        self.memo = {}
        return self.play(nums, 0, len(nums) - 1) >= 0

    def play(self, nums: list[int], first_one: int, last_one: int):
        if first_one == last_one:
            return nums[first_one]
        if (first_one, last_one) in self.memo:
            return self.memo[(first_one, last_one)]
        left_one, right_one = nums[first_one], nums[last_one]
        left = left_one - self.play(nums, first_one + 1, last_one)
        right = right_one - self.play(nums, first_one, last_one - 1)
        res = max(left, right)
        self.memo[(first_one, last_one)] = res
        return res