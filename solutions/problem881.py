class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        people.sort(reverse=True)
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                l += 1
            res += 1
        return res

s = Solution()
print(s.numRescueBoats([3,4,4,1], 5))