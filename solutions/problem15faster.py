class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(list(nums))
        triplets = []
        triplets_map = dict()
        for fixed_index in range(0, len(nums) - 2):
            left_index = fixed_index + 1
            right_index = len(nums) - 1
            while left_index < right_index:
                if nums[fixed_index] + nums[left_index] + nums[right_index] < 0:
                    left_index += 1
                elif nums[fixed_index] + nums[left_index] + nums[right_index] > 0:
                    right_index -= 1
                else:
                    string = str(nums[fixed_index])+','+str(nums[left_index])+','+str(nums[right_index])
                    if not(triplets_map.get(string)):
                        triplets.append([nums[fixed_index], nums[left_index], nums[right_index]])
                        triplets_map[string] = True
                    left_index += 1
                    right_index -= 1
s = Solution()
print(s.threeSum([0,0,0,0]))