class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        dp = [0] * (max(nums) + 1)
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + num
        minimum_num = min(nums)
        dp[minimum_num] = hash_map[minimum_num]
        for i in range(minimum_num + 1, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + hash_map.get(i, 0))
        return max(dp[-1], dp[-2])

s = Solution()
print(s.deleteAndEarn([2,2,3,3,3,4]))