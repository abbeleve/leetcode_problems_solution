from copy import copy

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        score_copy = copy(score)
        first_rank = score.index(max(score))
        score.pop(first_rank)
        second_rank = score.index(max(score))
        score.pop(second_rank)
        third_rank = score.index(max(score))
        res = []
        for i in range(len(score)):
            if i == first_rank:

