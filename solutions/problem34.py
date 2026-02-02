class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        target_index = self.binarySearch(nums, target)
        if target_index == -1:
            return [-1, -1]
        if nums[0] == target:
            lower_border = -1
        else:
            lower_border = self.findLowerBorder(nums, target_index, target)
        if nums[-1] == target:
            higher_border = len(nums)
        else:
            higher_border = self.findHigherBorder(nums, target_index, target)
        return [lower_border + 1, higher_border - 1]

    def findLowerBorder(self, nums: list[int], target_index: int, target: int) -> int:
        left_index, right_index = 0, target_index
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            if nums[mid_index + 1] == target and nums[mid_index] != target:
                return mid_index
            if nums[mid_index] < target:
                left_index = mid_index + 1
            elif nums[mid_index] == target:
                right_index = mid_index - 1

    def findHigherBorder(self, nums: list[int], target_index: int, target: int) -> int:
        left_index, right_index = target_index, len(nums) - 1
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            if nums[mid_index - 1] == target and nums[mid_index] != target:
                return mid_index
            if nums[mid_index] > target:
                right_index = mid_index - 1
            elif nums[mid_index] == target:
                left_index = mid_index + 1

    def binarySearch(self, nums: list[int], target: int) -> int:
        left_index, right_index = 0, len(nums) - 1
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            if nums[mid_index] > target:
                right_index = mid_index - 1
            elif nums[mid_index] < target:
                left_index = mid_index + 1
            else:
                return mid_index
        return -1

s = Solution()
print(s.searchRange(nums = [1, 1], target = 1))