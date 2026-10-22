class Solution:
    def numTeams(self, rating: list[int]) -> int:
        if rating is None or len(rating) < 3:
            return 0
        res = 0
        for middle_index in range(1, len(rating) - 1):
            left_less_than_middle = 0
            left_greater_than_middle = 0
            right_less_than_middle = 0
            right_greater_than_middle = 0
            for left_index in range(0, middle_index):
                if rating[left_index] < rating[middle_index]:
                    left_less_than_middle += 1
                elif rating[left_index] > rating[middle_index]:
                    left_greater_than_middle += 1
            for right_index in range(middle_index + 1, len(rating)):
                if rating[right_index] < rating[middle_index]:
                    right_less_than_middle += 1
                elif rating[right_index] > rating[middle_index]:
                    right_greater_than_middle += 1
            res += left_less_than_middle * right_greater_than_middle + left_greater_than_middle * right_less_than_middle
        return res
        