class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        set_of_numbers = set()
        hash_map = {}
        for array_index, array in enumerate(arrays):
            for num in array:
                set_of_numbers.add(num)
                if num not in hash_map:
                    hash_map[num] = [array_index]
                else:
                    hash_map[num].append(array_index)
        list_of_numbers = list(set_of_numbers)
        list_of_numbers.sort()
        l, r = 0, len(list_of_numbers) - 1
        if l == r:
            return 0
        while l < r:
            l_num, r_num = list_of_numbers[l], list_of_numbers[r]
            if len(hash_map[l_num]) >= 2 or len(hash_map[r_num]) >= 2:
                return r_num - l_num
            if hash_map[l_num][0] != hash_map[r_num][0]:
                return r_num - l_num
            if list_of_numbers[r] - list_of_numbers[l + 1] >= list_of_numbers[r - 1] - list_of_numbers[l]:
                l += 1
            else:
                r -= 1

s = Solution()
print(s.maxDistance(arrays = [[-10,-8,-8,-6,-4,4],[-4,-3]]))