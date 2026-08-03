# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        random_number_1 = rand7()
        while random_number_1 > 6:
            random_number_1 = rand7()
        if random_number_1 < 4:
            random_number_2 = rand7()
            while random_number_2 > 5:
                random_number_2 = rand7()
            return random_number_2
        else:
            random_number_2 = rand7()
            while random_number_2 > 5:
                random_number_2 = rand7()
            return random_number_2 + 5