class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        nums = [-1 if i == 0 else 1 for i in nums]
        prefix_sums = [0]
        for i in range(len(nums)):
            prefix_sums.append(prefix_sums[i] + nums[i])
        prefix_sums.pop(0)
        hash_map = {}
        for index, i in enumerate(prefix_sums):
            if i not in hash_map:
                hash_map[i] = [index]
            else:
                hash_map[i].append(index)
        keys = hash_map.keys()
        max_diff = 0
        for key in keys:
            if len(hash_map[key]) == 1:
                continue
            max_diff = max(max_diff, hash_map[key][-1] - hash_map[key][0])
        if 0 not in hash_map:
            return max_diff
        return max(max_diff, hash_map[0][-1] + 1)

s = Solution()
print(s.findMaxLength(nums = [0,0,1,0,0,0,1,1]))