class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.combinations = []
        self.nums = sorted(nums)
        for amount_of_elements in range(len(nums) + 1):
            self.amount_of_elements = amount_of_elements
            self.backtrack([], 0, 0)
        return self.combinations
        
    
    def backtrack(self, combination, amount_of_elements, index_start):
        if amount_of_elements == self.amount_of_elements:
            if combination not in self.combinations:
                self.combinations.append(combination[:])
                return
        
        for index, num in enumerate(self.nums):
            if index < index_start:
                continue
            if num not in combination:
                combination.append(num)
                amount_of_elements += 1
                self.backtrack(combination, amount_of_elements, index + 1)
                combination.pop()
                amount_of_elements -= 1

#easy solution with itertools

import itertools

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        item_list = list(nums) 
        all_subsets = []
        for i in range(len(item_list) + 1):
            for combo in itertools.combinations(item_list, i):
                all_subsets.append(list(combo))
        return all_subsets

s = Solution()
print(s.subsets([3,2,4,1]))