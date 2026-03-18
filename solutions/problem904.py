class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        if len(fruits) < 3:
            return len(fruits)
        fruit_1, fruit_2 = fruits[0], None
        left_index, right_index = 0, 0
        max_length = 0
        while right_index < len(fruits):
            fruit = fruits[right_index]
            right_index += 1
            max_length += 1
            if fruit != fruit_1:
                fruit_2 = fruit
                break
        if fruit_2 is None:
            return len(fruits)
        while right_index < len(fruits):
            fruit = fruits[right_index]
            if fruit != fruit_1 and fruit != fruit_2:
                left_index = right_index - 1
                base_fruit = fruits[left_index]
                while base_fruit == fruits[left_index]:
                    left_index -= 1
                left_index += 1
                fruit_1 = base_fruit
                fruit_2 = fruit
            right_index += 1
            max_length = max(max_length, right_index - left_index)
        return max_length
    
s = Solution()
print(s.totalFruit(fruits = [0,1,2,2]))