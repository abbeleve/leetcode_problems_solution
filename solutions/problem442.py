class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        hash_map = set()
        res = []
        for num in nums:
            if num in hash_map:
                res.append(num)
            else:
                hash_map.add(num)
        return res

s = Solution()
print(s.findDuplicates(nums = [4,3,2,7,8,2,3,1]))