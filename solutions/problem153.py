class Solution:
    def findMin(self, nums: list[int]) -> int:
        left_index, right_index = 0, len(nums) - 1
        division_index = 0
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            if mid_index == len(nums) - 1:
                division_index = len(nums) - 1
                break
            if nums[mid_index] > nums[mid_index + 1]:
                division_index = mid_index + 1
                break
            if nums[mid_index - 1] > nums[mid_index]:
                division_index = mid_index
                break
            if nums[mid_index] > nums[right_index]:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1
        return nums[division_index]

s = Solution()
print(s.findMin([11,13,15,17]))