import math

class Solution:
    def minSteps(self, n: int) -> int:
        result = 0
        if n == 1: return 0
        d = 2
        while d <= math.ceil(math.sqrt(n)):
            while n % d == 0:
                result += d
                n /= d
            d += 1
        if n > 1:
            result += n
        return int(result)
    
s = Solution()
print(s.minSteps(12))