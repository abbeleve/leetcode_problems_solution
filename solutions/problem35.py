class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            if nums[mid_index] > target:
                right_index = mid_index - 1
            elif nums[mid_index] < target:
                left_index = mid_index + 1
            else:
                return mid_index
        
        return left_index
            
s = Solution()
print(s.searchInsert([1,3,5,6], 5))