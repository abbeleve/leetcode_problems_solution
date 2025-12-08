class Solution:
    def isHappy(self, n: int) -> bool:
        remember_items = dict()
        while n != 1:
            new_n = self.replace_number(n)
            if remember_items.get(new_n) is not None:
                return False
            remember_items[new_n] = True
            n = new_n
        return True

    def replace_number(self, n: int) -> int:
        sums = 0
        while n > 0:
            sums += (n % 10) ** 2
            n //= 10
        return sums
    
s = Solution()
print(s.isHappy(19))