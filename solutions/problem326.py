class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n >= 1:
            while n > 1:
                if n % 3 != 0:
                    return False
                n //= 3
            if n == 1:
                return True
            return False
        else:
            epsilon = 10**5
            while n < 1:
                n *= 3
            if 1 - epsilon <= n <= 1 + epsilon:
                return True
            return False
        