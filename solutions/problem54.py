class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        direction = 0
        result = []
        while True:
            if len(matrix) == 1:
                if direction == 0:
                    result.extend(matrix[0])
                    return result
                elif direction == 1:
                    if len(matrix[0]) == 1:
                        result.append(matrix[0][0])
                        return result
                    result.append(matrix[0][-1])
                    matrix[0].pop()
                elif direction == 2:
                    result.extend(matrix[0][::-1])
                    return result
                elif direction == 3:
                    if len(matrix[0]) == 1:
                        result.append(matrix[0][0])
                        return result
                    result.append(matrix[0][0])
                    matrix[0].pop(0)
                continue
            elif len(matrix[0]) == 1:
                if direction == 0:
                    result.append(matrix[0][0])
                    matrix.pop(0)
                elif direction == 1:
                    result.extend([row[0] for row in matrix])
                    return result
                elif direction == 2:
                    result.append(matrix[-1][0])
                    matrix.pop()
                elif direction == 3:
                    add = [row[0] for row in matrix]
                    add.reverse()
                    result.extend(add)
                    return result
            else:
                if direction == 0:
                    result.extend(matrix[0])
                    matrix = matrix[1:]
                elif direction == 1:
                    result.extend([row[-1] for row in matrix])
                    matrix = [row[:-1] for row in matrix]
                elif direction == 2:
                    result.extend(matrix[-1][::-1])
                    matrix = matrix[:-1]
                elif direction == 3:
                    add = [row[0] for row in matrix]
                    add.reverse()
                    result.extend(add)
                    matrix = [row[1:] for row in matrix]
            direction += 1
            direction = direction % 4

s = Solution()
print(s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))