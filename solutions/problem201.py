class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        binary_left = bin(left)[2:]
        binary_right = bin(right)[2:]
        len_diff = len(binary_right) - len(binary_left)
        binary_right = binary_right[len_diff:]
        left = int(binary_left, 2)
        right = int(binary_right, 2)
        result = left
        for binaries in range(left + 1, right):
            result = result & binaries
        return result
    
s = Solution()
print(s.rangeBitwiseAnd(1, 2147483647))