class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        if len(pairs) == 1:
            return 1
        pairs.sort(key=lambda x: x[0])
        chain_length = 1
        length = len(pairs)
        index = 0
        while index < length - 1:
            pair_1, pair_2 = pairs[index], pairs[index + 1]
            if pair_1[1] < pair_2[0]:
                chain_length += 1
                index += 1
            else:
                if pair_1[1] <= pair_2[1]:
                    pairs.pop(index + 1)
                else:
                    pairs.pop(index)
                length -= 1
        return chain_length

s = Solution()
print(s.findLongestChain([[1,2],[2,3],[3,4]]))