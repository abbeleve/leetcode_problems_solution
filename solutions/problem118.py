class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(1, numRows + 1):
            res.append([1]*i)
        for i in range(2, len(res)):
            row = res[i]
            prev_row = res[i - 1]
            for j in range(1, len(row) - 1):
                row[j] = prev_row[j - 1] + prev_row[j]
        return res

s = Solution()
print(s.generate(5))