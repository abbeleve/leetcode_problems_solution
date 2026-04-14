class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        res = 0
        for num in nums:
            res = res ^ num
        diff = res & -res
        x = 0
        y = 0
        for num in nums:
            if num & diff:
                x ^= num
            else:
                y ^= num
        return [x, y]