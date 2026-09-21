class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        self.s = s
        self.good_combinations = set()
    
    def backtracking(combination):
        