class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        dp = [[float('inf') for _ in range(len(matrix))] for _ in range(len(matrix))]
        dp[0] = matrix[0]
        for i in range(1, len(matrix)):
            for j in range(len(matrix)):
                if j != 0:
                    dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i - 1][j - 1])
                dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i - 1][j])
                if j != len(matrix) - 1:
                    dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i - 1][j + 1])
        return min(dp[-1])

s = Solution()
print(s.minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]]))