class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        hash_map = {}
        cum_sum = 0
        res = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum % k == 0:
                res += 1
            res += hash_map.get(cum_sum % k, 0)
            hash_map[cum_sum % k] = hash_map.get(cum_sum % k, 0) + 1
        return res

s = Solution()
print(s.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))