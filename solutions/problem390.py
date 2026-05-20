class Solution:
    def lastRemaining(self, n: int) -> int:
        step = 2
        iter = 0
        l, r = 1, n
        while l != r:
            if l % step == r % step:
                l += step // 2
                r -= step // 2
            else:
                if iter % 2 == 0:
                    l += step // 2
                else:
                    r -= step // 2
            step *= 2
            iter += 1
        return l

s = Solution()
print(s.lastRemaining(9))