import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True for _ in range(n)]
        primes[0], primes[1] = False, False
        for num in range(2, math.ceil(math.sqrt(n))):
            if not(primes[num]):
                continue
            prime_num = num * 2
            while prime_num < n:
                primes[prime_num] = False
                prime_num = prime_num + num
        
        counter = 0
        for i in primes:
            if i:
                counter += 1
        return counter

s = Solution()
print(s.countPrimes(3))