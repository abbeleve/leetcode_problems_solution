class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        res = 0
        hash_map = {}
        each_index = {}
        for i in range(len(values)):
            if values[i] not in hash_map:
                hash_map[values[i]] = [labels[i]]
            else:
                hash_map[values[i]].append(labels[i])
            each_index[labels[i]] = 0
        values.sort(reverse=True)
        for i, value in enumerate(values):
            while len(hash_map[value]) > 0 and each_index[hash_map[value][-1]] >= useLimit:
                hash_map[value].pop()
            if len(hash_map[value]) > 0:
                res += value
                each_index[hash_map[value][-1]] += 1
                numWanted -= 1
                hash_map[value].pop()
            if numWanted == 0:
                break
        return res

s = Solution()
print(s.largestValsFromLabels([4,9,1,1,2], [2,2,1,2,2], 4, 2))