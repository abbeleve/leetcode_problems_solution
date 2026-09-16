class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        sum = 0
        elem = 1
        amount_of_steps = 0
        while sum + elem <= target:
            sum = sum + elem
            elem += 1
            amount_of_steps += 1
        if sum == target:
            return amount_of_steps
        return amount_of_steps + 2 * (target - sum)

s = Solution()
print(s.reachNumber(30))