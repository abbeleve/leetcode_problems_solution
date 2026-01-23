class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if nums[0] > nums[-1]:
            #Rotated array
            left, right = 0, len(nums) - 1
            while left <= right:
                