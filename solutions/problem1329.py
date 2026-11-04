class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = []
        for height in range(m - 1, -1 , -1):
            diagonals.append((height, 0))
        for width in range(1, n):
            diagonals.append((0, width))
        full_diagonals = []
        for height_start, width_start in diagonals:
            one_diagonal = []
            for offset in range(m):
                height = height_start + offset
                width = width_start + offset
                if height >= m or width >= n:
                    break
                one_diagonal.append(mat[height][width])
            full_diagonals.append(one_diagonal)
        full_diagonals = [sorted(i) for i in full_diagonals]
        for i, (height_start, width_start) in enumerate(diagonals):
            for offset in range(m):
                height = height_start + offset
                width = width_start + offset
                if height >= m or width >= n:
                    break
                mat[height][width] = full_diagonals[i][offset]
        return mat

s = Solution()
print(s.diagonalSort(mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]))