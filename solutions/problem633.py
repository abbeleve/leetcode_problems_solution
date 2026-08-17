import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        if c < 0:
            return False
        eps = 10**(-6)
        for a in range(1, math.ceil(math.sqrt(c)) + 1):
            try:
                b = math.sqrt(c - a**2)
            except:
                continue
            print(a, b)
            if int(b) - eps <= b <= int(b) + eps:
                print(a, b)
                return True
            if math.ceil(b) - eps <= b <= math.ceil(b) + eps:
                print(a, b)
                return True
        return False