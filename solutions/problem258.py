class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = str(num)
            new_num = 0
            for digit in num:
                new_num += int(digit)
            num = new_num
        return num