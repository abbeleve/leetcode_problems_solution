import heapq

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]
        hash_map = {0: [-10**5], 1: [nums[0]]}
        maximum_subsequence_length = 1
        for index, num in enumerate(nums[1:]):
            for subsequence_length in range(maximum_subsequence_length, -1, -1):
                subsequence_num = min(hash_map[subsequence_length])
                if num > subsequence_num:
                    if subsequence_length + 1 not in hash_map:
                        hash_map[subsequence_length + 1] = [num]
                        maximum_subsequence_length += 1
                    else:
                        hash_map[subsequence_length + 1].append(num)
                    break
        return maximum_subsequence_length

s = Solution()
print(s.lengthOfLIS([1,2,-10,-8,-7]))