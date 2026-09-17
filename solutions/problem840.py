class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        res = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                square_3_by_3 = [row[j:j+3] for row in grid[i:i+3]]
                if self.is_magical_square(square_3_by_3):
                    res += 1
        return res

    def is_magical_square(self, grid):
        all_numbers = set()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if not 1 <= grid[i][j] <= 9:
                    return False
                all_numbers.add(grid[i][j])
        if len(all_numbers) != 9:
            return False
        sums = sum(grid[0])
        for i in range(len(grid)):
            row_sum = 0
            for j in range(len(grid)):
                row_sum += grid[i][j]
            if sums != row_sum:
                return False
        for j in range(len(grid)):
            column_sum = 0
            for i in range(len(grid)):
                column_sum += grid[i][j]
            if sums != column_sum:
                return False
        diag_sum_1, diag_sum_2 = 0, 0
        for i in range(len(grid)):
            diag_sum_1 += grid[i][i]
            diag_sum_2 += grid[i][len(grid) - i - 1]
        return not (diag_sum_1 != sums or diag_sum_2 != sums)

s = Solution()
print(s.numMagicSquaresInside(grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]))