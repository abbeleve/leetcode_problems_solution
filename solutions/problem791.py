class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hash_map = {}
        for index, letter in enumerate(order):
            hash_map[letter] = index
        s = sorted(s, key = lambda x: hash_map.get(x, float('inf')))
        return "".join(s)

s = Solution()
print(s.customSortString('cba', 'abcd'))