class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        checked = [False] * len(nums)
        for index, num in enumerate(nums):
            if checked[index]:
                continue
            path = {}
            path[index] = 0
            pos_check_failed = False
            start_pos, next_pos, positivity, num_of_steps = index, (index + num) % len(nums), num > 0, 1
            while next_pos not in path:
                path[next_pos] = num_of_steps
                if (nums[next_pos] > 0) != positivity:
                    pos_check_failed = True
                    break
                next_pos += nums[next_pos]
                next_pos = next_pos % len(nums)
                num_of_steps += 1

            if path[next_pos] == num_of_steps - 1:
                continue
            if pos_check_failed:
                list_pos = list(path.keys())
                for pos in list_pos:
                    checked[pos] = True
                continue
            if len(path) > 1:
                return True
            else:
                list_pos = list(path.keys())
                for pos in list_pos:
                    checked[pos] = True
        return False

s = Solution()
print(s.circularArrayLoop(nums = [-1,-2,-3,-4,-5,6]))