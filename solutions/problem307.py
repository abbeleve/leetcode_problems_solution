class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.tree = [0 for _ in range(4*len(self.nums))]
        if len(nums) == 0:
            return
        def build_tree(index, left, right):
            if right - left == 1:
                self.tree[index] = self.nums[left]
                return self.nums[left]
            mid = (right + left) // 2
            left_sum = build_tree(2*index + 1, left, mid)
            right_sum = build_tree(2*index + 2, mid, right)
            node_sum = left_sum + right_sum
            self.tree[index] = node_sum
            return node_sum
        build_tree(0, 0, len(nums))
        print(self.tree)
        
    def update(self, index: int, val: int) -> None:
        self.update_recursive(0, 0, len(self.nums), index, val)
    
    def update_recursive(self, tree_index, node_l, node_r, index, new_val):
        if node_r - node_l == 1:
            self.tree[tree_index] = new_val
            self.nums[index] = new_val
            return

        mid = (node_l + node_r) // 2
        if index < mid:
            self.update_recursive(2 * tree_index + 1, node_l, mid, index, new_val)
        else:
            self.update_recursive(2 * tree_index + 2, mid, node_r, index, new_val)
        self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_range_recursive(0, 0, len(self.nums), left, right + 1)

    def sum_range_recursive(self, tree_index, node_l, node_r, left, right):
        if left <= node_l and right >= node_r:
            return self.tree[tree_index]
        if right <= node_l or left >= node_r:
            return 0
        mid = (node_l + node_r) // 2
        return self.sum_range_recursive(2 * tree_index + 1, node_l, mid, left, right) + self.sum_range_recursive(2 * tree_index + 2, mid, node_r, left, right)

s = NumArray([1,3,5])
# s.update(2, 3)
print(s.sumRange(0, 2))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)