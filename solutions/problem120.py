class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for index_row in range(1, len(triangle)):
            row = triangle[index_row]
            prev_row = triangle[index_row - 1]
            for index, elem in enumerate(row):
                if index == 0:
                    row[index] += prev_row[0]
                elif index == len(row) - 1:
                    row[index] += prev_row[len(prev_row) - 1]
                else:
                    row[index] += min(prev_row[index - 1], prev_row[index])
        return min(triangle[-1])

s = Solution()
print(s.minimumTotal([[-10]]))