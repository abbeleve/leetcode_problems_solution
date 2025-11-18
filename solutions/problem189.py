class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        save_nums = []
        for i in range(0, len(nums)):
            save_nums.append(nums[i])
        for i in range(len(nums)):
            right_index = (i + k) % len(nums)
            nums[right_index] = save_nums[i]

nums = [1,2,3,4,5,6,7]
s = Solution()
s.rotate(nums, 3)
print(nums)