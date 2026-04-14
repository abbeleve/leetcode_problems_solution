class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1 for _ in range(len(ratings))]

        for i in range(1, len(ratings) - 1):
            if ratings[i] > ratings[i - 1] and ratings[i] > ratings[i + 1]:
                