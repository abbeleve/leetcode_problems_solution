import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        number = ''
        for i in range(n):
            amount_of_permutation = math.factorial(n - i - 1)
            if k == 1 or k == 0:
                number = number + "".join(numbers)
                return number
            number_index = (k - 1) // amount_of_permutation
            number += numbers[number_index]
            numbers.pop(number_index)
            k = k - amount_of_permutation * number_index

s = Solution()
print(s.getPermutation(n = 3, k = 4))