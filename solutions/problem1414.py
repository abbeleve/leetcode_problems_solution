class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        if fib[-1] != k:
            fib.pop()
        index = len(fib) - 1
        res = 0
        while k > 0:
            res += 1
            k -= fib[index]
            if k <= 0:
                break
            while k < fib[index]:
                index -= 1
        return res

s = Solution()
print(s.findMinFibonacciNumbers(5))