class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cumsum_difference = 0
        for day in range(len(prices) - 1):
            price, price_next_day = prices[day], prices[day + 1]
            difference = price_next_day - price
            if difference >= 0:
                cumsum_difference += difference
        return cumsum_difference

s = Solution()
print(s.maxProfit([7,6,4,3,1]))