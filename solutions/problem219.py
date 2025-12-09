class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        duplicates_map = dict()
        for index, num in enumerate(nums):
            if duplicates_map.get(num) is not None:
                if abs(duplicates_map[num] - index) <= k:
                    return True
            duplicates_map[num] = index

        return False
    
s = Solution()
print(s.containsNearbyDuplicate(nums = [2,2], k = 3))