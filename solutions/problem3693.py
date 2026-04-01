class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        costs.insert(0, 0)
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            if i == 1:
                dp[i] = dp[i - 1] + costs[i] + 1**2
            elif i == 2:
                dp[i] = min(dp[i - 1] + costs[i] + 1**2, dp[i - 2] + costs[i] + 2**2)
            else:
                dp[i] = min(dp[i - 1] + costs[i] + 1**2, dp[i - 2] + costs[i] + 2**2, dp[i - 3] + costs[i] + 3**2)
        return dp[-1]

s = Solution()
print(s.climbStairs(n = 4, costs = [1,2,3,4]))