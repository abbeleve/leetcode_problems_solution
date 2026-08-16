class Solution:
    def getMoneyAmount(self, n: int) -> int:
        self.list = [None] * n
        self.recurse(0, 0, 1, n)
        res = 0
        print(self.list)
        for i in self.list:
            res += i[1]
        return res
        

    def recurse(self, index_in_tree, price, l, r):
        if r - l <= 0:
            return
        if index_in_tree >= len(self.list):
            return
        m = (l + r) // 2
        self.list[index_in_tree] = (m, price)
        self.recurse(2*index_in_tree + 1, price + 1, l, m)
        self.recurse(2*index_in_tree + 2, price + 1, m + 1, r)
    
s = Solution()
print(s.getMoneyAmount(10))