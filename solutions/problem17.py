class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        combinations = []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        

    def return_letter(self, digits, index):
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if index >= 4:
            return
        for letter in mapping[digits[index]]:
            
        if combinations.find()