class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) < 4:
            for index, num in enumerate(nums):
                if num == target:
                    return index
            return -1
        left_index = 0
        right_index = len(nums) - 1
        mid_index = (left_index + right_index) // 2
        division_index = 0
        while True:
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
                left_index = mid_index
            else:
                right_index = mid_index
            mid_index = (left_index + right_index) // 2
        left_index_left = 0
        right_index_left = division_index - 1
        left_index_right = division_index
        right_index_right = len(nums) - 1
        res = self.binarySearch(nums, left_index_left, right_index_left, target)
        if res != -1:
            return res
        res = self.binarySearch(nums, left_index_right, right_index_right, target)
        if res != -1:
            return res
        return -1
        
    def binarySearch(self, nums, left_index, right_index, target):
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
print(s.search(nums = [4,5,6,7,0,1,2], target = 7))