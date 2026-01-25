import heapq

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        zero = [-10**5]
        heapq.heapify(zero)
        ones = [nums[0]]
        heapq.heapify(ones)
        hash_map = {0: zero, 1: ones}
        maximum_subsequence_length = 1
        for index, num in enumerate(nums[1:]):
            for subsequence_length in range(maximum_subsequence_length, -1, -1):
                subsequence_num = hash_map[subsequence_length][0]
                if num > subsequence_num:
                    if subsequence_length + 1 not in hash_map:
                        hash_map[subsequence_length + 1] = [num]
                        maximum_subsequence_length += 1
                    else:
                        heapq.heappush(hash_map[subsequence_length + 1], num)
                    break
        return maximum_subsequence_length

s = Solution()
print(s.lengthOfLIS([1,2,-10,-8,-7]))