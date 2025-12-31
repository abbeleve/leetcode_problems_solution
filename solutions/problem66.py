class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        while True:
            if i == 0:
                if digits[i] + 1 == 10:
                    digits.insert(0, 1)
                    digits[1] = 0
                else:
                    digits[i] += 1
                break
            elif digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                break
            i -= 1
            
        return digits
    
s = Solution()
print(s.plusOne([1,2,3]))