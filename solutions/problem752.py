from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        stack = deque([('0000', 0)])
        deadends_hash_map = set(deadends)
        hash_map = {}
        while stack:
            combination, depth = stack.popleft()
            if combination in deadends_hash_map:
                continue
            if combination not in hash_map or hash_map[combination] > depth:
                hash_map[combination] = depth
            else:
                continue
            for index_in_string in range(4):
                if combination[index_in_string] == '0':
                    new_combination = combination[:index_in_string] + '1' + combination[index_in_string + 1:]
                    stack.append((new_combination, depth + 1))
                    new_combination = combination[:index_in_string] + '9' + combination[index_in_string + 1:]
                    stack.append((new_combination, depth + 1))
                elif combination[index_in_string] == '9':
                    new_combination = combination[:index_in_string] + '0' + combination[index_in_string + 1:]
                    stack.append((new_combination, depth + 1))
                    new_combination = combination[:index_in_string] + '8' + combination[index_in_string + 1:]
                    stack.append((new_combination, depth + 1))
                else:
                    new_combination = combination[:index_in_string] + str(int(combination[index_in_string]) + 1) + combination[index_in_string + 1:]
                    stack.append((new_combination, depth + 1))
                    new_combination = combination[:index_in_string] + str(int(combination[index_in_string]) - 1) + combination[index_in_string + 1:]
                    stack.append((new_combination, depth + 1))
        return hash_map.get(target, -1)
            
s = Solution()
print(s.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))