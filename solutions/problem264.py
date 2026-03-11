class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbers = {0: set([1])}
        i_level_list = [1]
        level = 1
        amount_of_ugly_numbers = 1
        while amount_of_ugly_numbers < n:
            uglyNumbers[level] = set()
            for num in i_level_list:
                two = num * 2
                three = num * 3
                five = num * 5
                if two not in uglyNumbers[level]:
                    uglyNumbers[level].add(two)
                    amount_of_ugly_numbers += 1
                    if amount_of_ugly_numbers == n:
                        return two
                if three not in uglyNumbers[level]:
                    uglyNumbers[level].add(three)
                    amount_of_ugly_numbers += 1
                    if amount_of_ugly_numbers == n:
                        return three
                if five not in uglyNumbers[level]:
                    uglyNumbers[level].add(five)
                    amount_of_ugly_numbers += 1
                    if amount_of_ugly_numbers == n:
                        return five
            i_level_list = list(uglyNumbers[level])
            level += 1
        
s = Solution()
print(s.nthUglyNumber(10))