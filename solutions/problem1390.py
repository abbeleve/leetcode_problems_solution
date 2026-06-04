import math

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            sum_delit, amount_of_delit = num + 1, 2
            # if num % int(math.sqrt(num)) == 0:
            #     continue
            for delit in range(2, int(math.sqrt(num)) + 1):
                if num % delit == 0:
                    if delit != num // delit:
                        amount_of_delit += 2
                        sum_delit += delit
                        sum_delit += num // delit
                    else:
                        amount_of_delit += 4
                        break
                if amount_of_delit > 4:
                    break
            if amount_of_delit == 4:
                result += sum_delit
                print(f"good num: {num}")
        return result

s = Solution()
print(s.sumFourDivisors(nums = [1,2,3,4,5,6,7,8,9,10]))