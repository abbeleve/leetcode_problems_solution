class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [10**10 for _ in range(len(nums))]
        dp[0] = 0
        for index in range(0, len(dp)):
            for step in range(1, nums[index] + 1):
                if index + step >= len(dp):
                    break
                dp[index + step] = min(dp[index + step], dp[index] + 1)
        return dp[-1]
    
s = Solution()
print(s.jump(nums = [2,3,0,1,4]))