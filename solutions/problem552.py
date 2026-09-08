import sys

sys.setrecursionlimit(10**6)

class Solution:
    def checkRecord(self, n: int) -> int:
        self.n = n
        self.dp = [[[None for ___ in range(2)] for __ in range(3)] for _ in range(n)]
        self.res = 0
        return self.recurse(0, 0, False)
    
    def recurse(self, num_step: int, amount_of_L: int, was_A: bool):
        if num_step == self.n:
            return 1
        amount_of_vars = 0
        if self.dp[num_step][amount_of_L][was_A] is not None:
            return self.dp[num_step][amount_of_L][was_A]
        if not(was_A):
            amount_of_vars += self.recurse(num_step + 1, 0, True)
        if amount_of_L < 2:
            amount_of_vars += self.recurse(num_step + 1, amount_of_L + 1, was_A)
        amount_of_vars += self.recurse(num_step + 1, 0, was_A)
        self.dp[num_step][amount_of_L][was_A] = amount_of_vars
        return amount_of_vars % (10**9 + 7)

s = Solution()
print(s.checkRecord(100000))