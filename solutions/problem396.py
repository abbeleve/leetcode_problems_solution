class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        sums = sum(nums) - nums[0]
        clockwise_sums = sum([i*nums[i] for i in range(len(nums))])
        result = max(float('-inf'), clockwise_sums)
        for i in range(1, len(nums)):
            clockwise_sums = clockwise_sums - sums + (len(nums) - 1) * nums[i - 1]
            sums = sums - nums[i] + nums[i - 1]
            result = max(result, clockwise_sums)
        return result
    
s = Solution()
print(s.maxRotateFunction(nums = [4,3,2,6]))
