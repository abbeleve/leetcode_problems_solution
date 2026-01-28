class Solution:
    def mySqrt(self, x: int) -> int:
        save_x = x
        power = 0
        while x > 10:
            x /= 10
            power += 1
        lower_bound = 1
        power = power // 2
        for i in range(power):
            lower_bound = lower_bound * 10

        root = 0
        for i in range(lower_bound, lower_bound * 100):
            if i*i <= save_x:
                root = i
            else:
                break
        return root


s = Solution()
print(s.mySqrt(13453145))