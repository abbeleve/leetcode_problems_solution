class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        dp = [False for _ in range(sum(nums) // 2 + 1)]
        dp[0] = True
        for num in reversed(nums):
            for index in range(len(dp) - 1, -1, -1):
                dynamic = dp[index]
                if dynamic and index + num < len(dp):
                    dp[index + num] = True
                    if index + num == len(dp) - 1:
                        return True
            if num < len(dp):
                dp[num] = True
            if num == len(dp) - 1:
                return True
        return False

s = Solution()
print(s.canPartition([2,2,3,5]))