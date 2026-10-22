class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        strs = [[i.count('0'), i.count('1')] for i in strs]
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for __ in range(len(strs) + 1)]
        for i in range(1, len(strs) + 1):
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - strs[i - 1][0]][k - strs[i - 1][1]] + 1 if j >= strs[i - 1][0] and k >= strs[i - 1][1] else 0)
        return dp[-1][-1][-1]