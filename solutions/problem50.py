class Solution:
    def myPow(self, x: float, n: int) -> float:
        base = x
        if n == 0:
            return 1
        
        znak = n >= 0

        n = abs(n)
        
        while abs(n) > 1:
            x = x * x
            if n % 2 == 1:
                x = x * base
            n = n // 2

        if znak:
            return x
        return 1 / x
    
s = Solution()
print(s.myPow(8.84372, -5))