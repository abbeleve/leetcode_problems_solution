class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * target for _ in range(n)]
        for i in range(min(k, target)):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(1, target):
                sums = 0
                for offset in range(1, k + 1):
                    if j - offset >= 0:
                        sums += dp[i - 1][j - offset]
                    else:
                        break
                dp[i][j] = sums
        return dp[-1][target - 1] % (10**9 + 7)
        
s = Solution()
print(s.numRollsToTarget(30, 30, 500))