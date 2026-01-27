class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, num + current_sum)
            max_sum = max(current_sum, max_sum)
        return max_sum
    
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))