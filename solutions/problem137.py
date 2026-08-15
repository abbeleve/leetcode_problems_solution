class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = "0"
        minimal_nums = min(nums)
        if minimal_nums < 0:
            minimal_nums = minimal_nums * (-1)
            for i in range(len(nums)):
                nums[i] += minimal_nums
        else:
            minimal_nums = None
        for num in nums:
            ternary = self.to_ternary(num)
            res = self.sum_two_ternary_numbers(res, ternary)
        return int(res, 3) - minimal_nums if minimal_nums is not None else int(res, 3)


    def to_ternary(self, n: int) -> str:
        if n == 0:
            return '0'
        res = ''
        while n > 0:
            res += str(n % 3)
            n //= 3
        return res[::-1]

    def sum_two_ternary_numbers(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num2 = "0" * (len(num1) - len(num2)) + num2
        res = ""
        for i in range(len(num1) - 1, -1, -1):
            res = str((int(num1[i]) + int(num2[i])) % 3) + res
        return res

s = Solution()
print(s.singleNumber(nums = [-2,-2,1,1,4,1,4,4,-4,-2]))