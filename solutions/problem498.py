class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if len(mat) == 0:
            return
        if len(mat) == 1:
            return mat[0]
        amount_of_diagonales, i, j = 2 * len(mat) - 1, 0, 1
        diaganole = 0
        result = [mat[0][0]]
        while diaganole < amount_of_diagonales - 1:
            diaganole += 1
            if diaganole <= len(mat) - 1:
                if diaganole % 2 == 0:
                    while i != -1:
                        result.append(mat[i][j])
                        i -= 1
                        j += 1
                    i += 1
                else:
                    while j != -1:
                        result.append(mat[i][j])
                        j -= 1
                        i += 1
                    j += 1
            if diaganole == len(mat) - 1:
                if len(mat) % 2 == 1:
                    i += 1
                    j -= 1
                else:
                    j += 1
                    i -= 1
            if diaganole > len(mat) - 1:
                if diaganole % 2 == 0:
                    while j != len(mat) - 1:
                        result.append(mat[i][j])
                        i -= 1
                        j += 1
                    result.append(mat[i][j])
                    i += 1
                else:
                    while i != len(mat) - 1:
                        result.append(mat[i][j])
                        j -= 1
                        i += 1
                    result.append(mat[i][j])
                    j += 1
        return result
    
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        result = []
        fast_result = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j >= len(fast_result):
                    fast_result.append([mat[i][j]])
                else:
                    fast_result[i + j].append(mat[i][j])
        for index, elem in enumerate(fast_result):
            if index % 2 == 0:
                fast_result[index].reverse()
                result.extend(fast_result[index])
            else:
                result.extend(fast_result[index])
        return result
    
s = Solution()
print(s.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))