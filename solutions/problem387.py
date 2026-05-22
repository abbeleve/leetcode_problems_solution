class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        order = []
        for i in s:
            if i not in hash_map:
                hash_map[i] = 1
                order.append(i)
            else:
                hash_map[i] += 1
        for i in order:
            if hash_map[i] == 1:
                return s.index(i)
        return -1