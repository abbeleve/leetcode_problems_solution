class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(list(nums))
        left_index = 0
        right_index = len(nums) - 1
        triplets = []
        triplets_map = dict()
        for middle_index in range(1, len(nums) - 1):
            left_index = 0
            right_index = len(nums) - 1
            while left_index < right_index and left_index < middle_index and right_index > middle_index:
                if nums[left_index] + nums[middle_index] + nums[right_index] < 0:
                    left_index += 1
                elif nums[left_index] + nums[middle_index] + nums[right_index] > 0:
                    right_index -= 1
                else:
                    string = str(nums[left_index])+','+str(nums[middle_index])+','+str(nums[right_index])
                    if not(triplets_map.get(string)):
                        triplets.append([nums[left_index], nums[middle_index], nums[right_index]])
                        triplets_map[string] = True
                    # while left_index + 1 < middle_index and nums[left_index + 1] == nums[left_index]:
                    #     left_index += 1
                    # while right_index - 1 > middle_index and nums[right_index - 1] == nums[right_index]:
                    #     right_index -= 1

                    left_index += 1
                    right_index -= 1
                    
        return triplets
            
s = Solution()
print(s.threeSum([0,0,0,0]))