class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        counter = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if dp[i] + 1 > dp[j]:
                        dp[j] = dp[i] + 1
                        counter[j] = counter[i]
                    elif dp[i] + 1 == dp[j]:
                        counter[j] += counter[i]
        max_length = max(dp)
        result = 0
        for i in range(len(nums)):
            if dp[i] == max_length:
                result += counter[i]
        return result

s = Solution()
print(s.findNumberOfLIS([1,1,1,2,2,2,3,3,3]))