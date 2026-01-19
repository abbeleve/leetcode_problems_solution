class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return nums.index(max(nums))
        left, right = 0, len(nums) - 1
        if nums[left] > nums[left + 1]:
            return left
        if nums[right] > nums[right - 1]:
            return right
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left