class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0]*n for i in range(n)]
        i, j, D = 0, 0, 'R'
        num = 1
        while num < n**2 + 1:
            if D == 'R':
                if j == n or matrix[i][j] != 0:
                    D = 'D'
                    j -= 1
                    i += 1
                else:
                    matrix[i][j] = num
                    num += 1
                    j += 1
            elif D == 'D':
                if i == n or matrix[i][j] != 0:
                    D = 'L'
                    i -= 1
                    j -= 1
                else:
                    matrix[i][j] = num
                    num += 1
                    i += 1
            elif D == 'L':
                if j == -1 or matrix[i][j] != 0:
                    D = 'U'
                    j += 1
                    i -= 1
                else:
                    matrix[i][j] = num
                    num += 1
                    j -= 1
            elif D == 'U':
                if i == -1 or matrix[i][j] != 0:
                    D = 'R'
                    i += 1
                    j += 1
                else:
                    matrix[i][j] = num
                    num += 1
                    i -= 1
            
        return matrix

s = Solution()
print(s.generateMatrix(n = 7))