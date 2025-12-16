class Solution:
    def reverseBits(self, n: int) -> int:
        binary_form = bin(n)[2:]
        binary_form = "0"*(32 - len(binary_form)) + binary_form
        return int(binary_form[::-1], 2)
    
s = Solution()
print(s.reverseBits(43261596))

