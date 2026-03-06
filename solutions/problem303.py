class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.suffix_sums = [0]
        for i, num in enumerate(nums):
            self.suffix_sums.append(self.suffix_sums[i] + num)
        self.prefix_sums = [0]
        for i, num in enumerate(nums):
            self.prefix_sums.append(self.prefix_sums[i] + num)

    def sumRange(self, left: int, right: int) -> int:
        suffix_sum = self.suffix_sums[right + 1]
        prefix_sum = self.prefix_sums[left]
        return suffix_sum - prefix_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)