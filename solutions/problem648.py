class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        res = ""
        for word in sentence.split():
            root_length = 10**9
            rooted = None
            for root in dictionary:
                if word.startswith(root):
                    if len(root) < root_length:
                        root_length = len(root)
                        rooted = root
            if rooted:
                res += " " + rooted
            else:
                res += " " + word
        return res[1:]

s = Solution()
print(s.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))