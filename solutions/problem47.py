class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        self.nums = nums
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        self.permuatations = []
        self.backtrack([], hash_map)
        return list(self.permuatations)

    def backtrack(self, permutation, hash_map):
        if len(permutation) == len(self.nums):
            if permutation not in self.permuatations:
                self.permuatations.append(permutation[:])
                return
        
        for num in hash_map.keys():
            if hash_map[num] == 0:
                continue
            permutation.append(num)
            hash_map[num] -= 1
            self.backtrack(permutation, hash_map)
            permutation.pop()
            hash_map[num] += 1

s = Solution()
print(s.permuteUnique([1,1,1,1,1,1,1,2]))