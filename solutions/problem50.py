class Solution:
    def myPow(self, x: float, n: int) -> float:
        base = x
        if n == 0:
            return 1
        
        znak = n >= 0

        n = abs(n)
        odd_multiplier = 1
        
        while n > 1:
            x = x * x
            if n % 2 == 1:
                odd_multiplier *= base
            n = n // 2
            base = x
        
        x *= odd_multiplier
        if znak:
            return x
        return 1 / x
    
s = Solution()
print(s.myPow(2, 5))