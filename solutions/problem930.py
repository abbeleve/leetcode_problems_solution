from collections import Counter

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_sums = [0]
        for i, num in enumerate(nums):
            prefix_sums.append(num + prefix_sums[-1])
        res = 0
        prefix_sums_set = Counter()
        for i in range(len(prefix_sums)):
            res += prefix_sums_set[prefix_sums[i] - goal]
            prefix_sums_set[prefix_sums[i]] += 1
        return res

s = Solution()
print(s.numSubarraysWithSum([0,0,0,0,0], 0))    