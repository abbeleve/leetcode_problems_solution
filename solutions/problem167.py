class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        first_pointer = 0
        last_pointer = len(numbers) - 1
        while first_pointer < last_pointer:
            if (numbers[first_pointer] + numbers[last_pointer]) == target:
                return first_pointer + 1, last_pointer + 1
            if (numbers[first_pointer] + numbers[last_pointer]) < target:
                first_pointer += 1
            else:
                last_pointer -= 1

s = Solution()
print(s.twoSum([2,7,11,15], 9))
