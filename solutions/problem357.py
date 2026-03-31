class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        if n == 0:
            return 1
        dp[1] = 0
        if n == 1:
            return 10
        dp[2] = 9
        if n == 2:
            return pow(10, n) - 9
        for i in range(3, len(dp)):
            dp[i] = dp[i - 1] * 10 * i
        return pow(10, n) - dp[-1]
    
s = Solution()
print(s.countNumbersWithUniqueDigits(3))