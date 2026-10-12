from copy import copy

class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        dp = copy(matrix)
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
        res = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                res += dp[i][j]
        return res

s = Solution()
print(s.countSquares(matrix =
[[1,0,1],[1,1,0],[1,1,0]]))