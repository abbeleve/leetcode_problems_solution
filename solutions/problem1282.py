class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = []
        group_indexes = {}
        for someone_index, group_size in enumerate(groupSizes):
            if group_size not in group_indexes:
                group_indexes[group_size] = len(groups)
                groups.append([])
            elif len(groups[group_indexes[group_size]]) == group_size:
                group_indexes[group_size] = len(groups)
                groups.append([])
            groups[group_indexes[group_size]].append(someone_index)
        return groups

s = Solution()
print(s.groupThePeople(groupSizes = [3,3,3,3,3,1,3]))