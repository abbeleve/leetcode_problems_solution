class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        hash_map = {}
        max_num = max(nums)
        for num in nums:
            hash_map[num] = 0
        for num in nums:
            if num not in hash_map:
                continue
            for next_number in range(num + 1, max_num + 1):
                if next_number in hash_map:
                    if hash_map[next_number] != 0:
                        if hash_map[num] == 0:
                            hash_map[num] += hash_map[next_number] + 1
                        else:
                            hash_map[num] += hash_map[next_number]
                        hash_map.pop(next_number)
                        break
                    else:
                        hash_map.pop(next_number)
                        if hash_map[num] == 0:
                            hash_map[num] += 2
                        else:
                            hash_map[num] += 1
                else:
                    if hash_map[num] == 0:
                        hash_map[num] += 1
                    break
        
        max_sequence_length = 1
        for key in list(hash_map.keys()):
            max_sequence_length = max(max_sequence_length, hash_map[key])
        return max_sequence_length
    
s = Solution()
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))