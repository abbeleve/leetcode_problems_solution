class Solution:
    def reverse(self, x: int) -> int:
        left_border = -2**31
        right_border = 2**31 - 1
        multiplier = 1
        if x < 0:
            multiplier = -1
        x = str(abs(x))
        x = multiplier * int(x[::-1])
        if left_border <= x <= right_border:
            return x
        return 0
    
s = Solution()
print(s.reverse(-13131313133131311313131313131313133113))