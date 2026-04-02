class Solution:
    def canCross(self, stones: list[int]) -> bool:
        self.stones = stones
        self.memo = set()
        self.hash_map = {}
        for index, stone in enumerate(stones):
            self.hash_map[stone] = index
        if self.recurse(0, 1):
            return True
        return False

    def recurse(self, position, jump_length):
        if jump_length == 0:
            return False
        if (position, jump_length) in self.memo:
            return False
        new_pos = position + jump_length
        if new_pos in self.hash_map:
            position = new_pos
            if self.hash_map[new_pos] == len(self.stones) - 1:
                return True
        else:
            return False
        if not(self.recurse(position, jump_length - 1)):
            self.memo.add((position, jump_length - 1))
        else:
            return True
        if not(self.recurse(position, jump_length)):
            self.memo.add((position, jump_length))
        else:
            return True
        if not(self.recurse(position, jump_length + 1)):
            self.memo.add((position, jump_length + 1))
        else:
            return True

s = Solution()
print(s.canCross(stones = [0,1,3,5,6,8,12,17]))