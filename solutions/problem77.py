#17% beated
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.combinations = []
        self.hash_map_combinations = {}
        self.backtrack([], n, k)
        return self.combinations

    def backtrack(self, combination, n, k):
        if len(combination) == k:
            self.combinations.append(combination)
            return
        if len(combination) > 0:
            last_elem = combination[-1]
        else:
            last_elem = 0
        for var in range(last_elem + 1, n + 1):
            new_combination = [i for i in combination]
            new_combination.append(var)
            self.backtrack(new_combination, n, k)
            # if new_combination not in self.combinations:
            #     self.backtrack(new_combination, n, k)
    
#77.52% beated
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.combinations = []
        self.hash_map_combinations = {}
        self.backtrack([], n, k)
        return self.combinations

    def backtrack(self, combination, n, k):
        if len(combination) == k:
            self.combinations.append(combination[:])
            return
        if len(combination) > 0:
            last_elem = combination[-1]
        else:
            last_elem = 0
        for var in range(last_elem + 1, n + 1):
            combination.append(var)
            self.backtrack(combination, n, k)
            combination.pop()

s = Solution()
print(s.combine(4, 2))