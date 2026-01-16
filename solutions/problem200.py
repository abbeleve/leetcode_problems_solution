class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        amount_of_islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                elem = grid[y][x]
                if elem == '0':
                    continue
                stack = [{'x': x, 'y': y}]
                grid[y][x] = 0
                while len(stack) > 0:
                    elem = stack.pop(0)
                    grid[elem['y']][elem['x']] = '0'
                    sideIndexes = self.getSideIndexes(elem, len(grid[0]), len(grid))
                    for x_, y_ in sideIndexes:
                        if x_ < 0 or y_ < 0:
                            continue
                        if x_ > len(grid[0]) - 1 or y_ > len(grid) - 1:
                            continue
                        neighbour_elem = grid[y_][x_]
                        if neighbour_elem == '0':
                            continue
                        grid[y_][x_] = '0'
                        stack.append({'x': x_, 'y': y_})
                amount_of_islands += 1
                
        
        return amount_of_islands
    
    def getSideIndexes(self, element: dict, x_len: int, y_len: int) -> list[tuple]:
        x, y = element['x'], element['y']
        possible_indexes = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return possible_indexes
    
s = Solution()
print(s.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
