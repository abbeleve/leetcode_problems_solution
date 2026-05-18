import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        l, r = 1, max(quantities)
        if n == len(quantities):
            return max(quantities)
        quantities.sort(reverse=True)
        while l <= r:
            mid = (l + r) // 2
            amount_of_products = mid
            diff = n - len(quantities)
            for index, product_quantity in enumerate(quantities):
                if product_quantity <= amount_of_products:
                    break
                division = math.ceil(product_quantity / amount_of_products) - 1
                diff -= division
                if diff < 0:
                    break
            if diff < 0:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
s = Solution()
print(s.minimizedMaximum(22, [25,11,29,6,24,4,29,18,6,13,25,30]))