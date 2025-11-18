class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        local_maximum = max(prices)
        index_of_local_maximum = prices.index(local_maximum)
        index = 0
        maximum_stock_difference = 0
        while index < len(prices) - 1:
            if prices[index] < prices[index + 1]:
                if index <= index_of_local_maximum:
                    maximum_stock_difference = max(maximum_stock_difference, local_maximum - prices[index])
                else:
                    local_maximum = max(prices[index + 1:])
                    index_of_local_maximum = prices[index + 1:].index(local_maximum) + index + 1
                    maximum_stock_difference = max(maximum_stock_difference, local_maximum - prices[index])
            index += 1
            
        return maximum_stock_difference


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))

# print([7,1,5,3,6,4][2:].index(6))