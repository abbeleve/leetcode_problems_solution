class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        saved_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[saved_index]:
                saved_index += 1
                nums[saved_index] = nums[i]
                
        
        return saved_index + 1

nums = [1,1,1,2,2,3]
s = Solution()
print(s.removeDuplicates(nums))
print(nums)