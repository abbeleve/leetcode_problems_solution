class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        max_possible_side = min(len(matrix), len(matrix[0]))
        dp = [[0 for __ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        maximum = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i - 1][j - 1] == '0':
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                if dp[i][j] > maximum:
                    maximum = dp[i][j]
        return maximum * maximum

s = Solution()
print(s.maximalSquare([["0","1"],["1","0"]]))