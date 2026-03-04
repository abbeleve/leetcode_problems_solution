class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        nums_ = [nums[i % len(nums)] for i in range(len(nums) * 2)]
        monotonic_stack = []
        elems = [-1 for i in range(len(nums_))]
        for index, num in enumerate(nums_):
            while monotonic_stack and nums_[index] > nums_[monotonic_stack[-1]]:
                elems[monotonic_stack[-1]] = nums[index % len(nums)]
                monotonic_stack.pop()
            monotonic_stack.append(index)
        return elems[0:len(nums)]
    
s = Solution()
print(s.nextGreaterElements([2, 5, 1, 4, 2]))