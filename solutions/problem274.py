class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        for index in range(len(citations)):
            