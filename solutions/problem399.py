class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        possible_letters = set()
        for i, j in equations:
            possible_letters.add(i)
            possible_letters.add(j)
        