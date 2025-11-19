import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        base = 5
        for power_of_base in range(1, 1000):
            delimeter = pow(base, power_of_base)
            if delimeter > n:
                break
            else:
                res += n // delimeter
        return res
    
s = Solution()
print(s.trailingZeroes(30))
print(math.factorial(30))
