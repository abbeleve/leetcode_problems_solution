class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        grumpy_loss = [grumpy[i] * customers[i] for i in range(len(grumpy))]
        customers = [(1 - grumpy[i]) * customers[i] for i in range(len(grumpy))]
        a = 0
        window_sum = sum(grumpy_loss[a:a+minutes])
        max_sum = window_sum
        a += 1
        while a + minutes <= len(grumpy_loss):
            window_sum = window_sum - grumpy_loss[a - 1] + grumpy_loss[a + minutes - 1]
            max_sum = max(max_sum, window_sum)
            a += 1
        return int(sum(customers) + max_sum)

s = Solution()
print(s.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3))