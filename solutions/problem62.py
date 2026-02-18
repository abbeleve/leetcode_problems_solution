class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        grid = [[0 for i in range(n)] for i in range(m)]
        grid[0][0] = 1
        for i in range(m):
            grid[i][0] = 1
        for i in range(n):
            grid[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]
    
s = Solution()
print(s.uniquePaths(m = 3, n = 7))