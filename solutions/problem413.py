class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        dp = [1 for _ in range(len(nums))]
        dp[1] = 2
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 2
        result = 0
        for i in range(1, len(dp)):
            if dp[i] >= 3:
                result += dp[i] - 2
        return result

s = Solution()
print(s.numberOfArithmeticSlices([1,2,3,8,9,10]))