class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        dp[0] = 0
        for i in range(2, n + 1):
            combination_amount = 0
            for j in range(1, i + 1):
                left_subtree = max(1, dp[j - 1])
                right_subtree = max(1, dp[i - j])
                combination_amount += left_subtree * right_subtree
            dp[i] = combination_amount
        return dp[-1]

s = Solution()
print(s.numTrees(4))