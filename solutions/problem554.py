class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        hash_map = {}
        height = len(wall)
        for index, row in enumerate(wall):
            if len(row) <= 1:
                continue
            new_row = [row[0]]
            hash_map[row[0]] = hash_map.get(row[0], 0) + 1
            for i in range(1, len(row) - 1):
                new_num = row[i] + new_row[i - 1]
                new_row.append(new_num)
                hash_map[new_num] = hash_map.get(new_num, 0) + 1
            wall[index] = new_row
        index_list = list(hash_map.keys())
        maximum_height = 0
        for i in index_list:
            maximum_height = max(maximum_height, hash_map[i])
        return height - maximum_height

s = Solution()
print(s.leastBricks(wall = [[1,1],[2],[1,1]]))