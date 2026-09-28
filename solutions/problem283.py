class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        amount_of_zeros = 0
        while index < len(nums):
            if nums[index] == 0:
                nums.pop(index)
                amount_of_zeros += 1
            else:
                index += 1
        nums.extend([0 for _ in range(amount_of_zeros)])
        return nums

s = Solution()
print(s.moveZeroes([0,0,1]))