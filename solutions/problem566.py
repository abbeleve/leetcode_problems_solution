class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        res = [[None] * c for _ in range(r)]
        sum_length = r * c
        if sum_length != len(mat[0]) * len(mat):
            return mat
        for i in range(sum_length):
            res_index = (i // c, i % c)
            mat_index = (i // len(mat[0]), i % len(mat[0]))
            res[res_index[0]][res_index[1]] = mat[mat_index[0]][mat_index[1]]
        return res

s = Solution()
print(s.matrixReshape([[1,2],[3,4]], 2, 4))