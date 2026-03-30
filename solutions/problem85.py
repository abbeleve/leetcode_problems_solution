class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        dp = [[0 for __ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1