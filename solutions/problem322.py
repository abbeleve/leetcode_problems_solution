# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:
#         MAXIMAL_AMOUNT_OF_COINS = 10**9
#         dp = [MAXIMAL_AMOUNT_OF_COINS for _ in range(amount + 1)]
#         dp[0] = 0
#         processed_indexes = [0]
#         for i in range(len(coins) - 1, -1, -1):
#             coin = coins[i]
#             for index in processed_indexes:
#                 next_index = index + coin
#                 if next_index > amount:
#                     continue
#                 if dp[next_index] == MAXIMAL_AMOUNT_OF_COINS:
#                     processed_indexes.append(next_index)
#                 dp[next_index] = min(1 + dp[index], dp[next_index])

#         if dp[-1] == MAXIMAL_AMOUNT_OF_COINS:
#             dp[-1] = -1
#         return dp[-1]
    
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        MAXIMAL_AMOUNT_OF_COINS = 10**9
        dp = [[0 if _ == 0 else MAXIMAL_AMOUNT_OF_COINS for _ in range(amount + 1)] for _ in range(len(coins))]
        for j in range(coins[0], len(dp[0]), coins[0]):
            dp[0][j] = dp[0][j - coins[0]] + 1
        for coin_index in range(1, len(dp)):
            coin = coins[coin_index]
            for j in range(1, len(dp[0])):
                if j >= coin:
                    dp[coin_index][j] = min(dp[coin_index - 1][j], dp[coin_index][j - coin] + 1)
                else:
                    dp[coin_index][j] = dp[coin_index - 1][j]
        if any(i[-1] != MAXIMAL_AMOUNT_OF_COINS for i in dp):
            return min(i[-1] for i in dp)
        return -1

s = Solution()
print(s.coinChange([2], amount=3))