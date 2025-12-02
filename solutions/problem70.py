import math

class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0
        min_sequence_length = n // 2 + n % 2
        for sequence_length in range(n, min_sequence_length - 1, -1):
            amount_of_twos = n - sequence_length
            Cnk = math.factorial(sequence_length) / (math.factorial(amount_of_twos) * math.factorial(sequence_length - amount_of_twos))
            result += Cnk

        return result
        
s = Solution()
print(s.climbStairs(2))