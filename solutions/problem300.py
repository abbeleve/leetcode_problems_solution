class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]
        hash_map = {1: [0]}
        maximum_subsequence_length = 1
        for index, num in enumerate(nums[1:]):
            for subsequence_length in range(maximum_subsequence_length, 0, -1):
                for subsequence_index in hash_map[subsequence_length]:
                    if num > nums[subsequence_index]:
                        if subsequence_length + 1 not in hash_map:
                            hash_map[subsequence_length + 1] = [subsequence_index]
                            maximum_subsequence_length += 1
                            break
                        else:
                            hash_map[subsequence_length + 1].append(subsequence_index)
        print(dp)
        print(hash_map)

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))