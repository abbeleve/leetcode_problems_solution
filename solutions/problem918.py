class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        
        def kadane(nums):
            max_sum = nums[0]
            current_sum = nums[0]
            for num in nums[1:]:
                current_sum = max(num, num + current_sum)
                max_sum = max(current_sum, max_sum)
            return max_sum
        
        def min_kadane(nums):
            min_sum = current_sum = nums[0]
            for num in nums[1:]:
                current_sum = min(num, num + current_sum)
                min_sum = min(current_sum, min_sum)
            return min_sum
        
        overall_sum = sum(nums)
        max_sum = kadane(nums)
        min_sum = min_kadane(nums)

        if max_sum < 0:
            return max_sum

        return max(max_sum, overall_sum - min_sum)
            
s = Solution()
print(s.maxSubarraySumCircular([5,-3,5]))