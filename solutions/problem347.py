class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        set_nums = list(hash_map.keys())
        set_nums.sort(key=lambda x: hash_map[x], reverse=True)
        return set_nums[:k]
    
s = Solution()
print(s.topKFrequent([1,2,1,2,1,2,1,1,3,3,2], k = 2))