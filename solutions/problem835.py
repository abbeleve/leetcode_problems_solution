class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        h, w = len(img1), len(img1)
        img1_larger = [[0 for _ in range(h * 3)] for __ in range(h * 3)]
        for i in range(h):
            for j in range(h):
                if img1[i][j] == 1:
                    img1_larger[i + h][j + h] = img1[i][j]
        window_coors = (h, h)
        best_res = 0
        for dy in range(-h, h):
            for dx in range(-h, h):
                y, x = window_coors
                windowed_img1 = [row[x + dx: x + dx + h] for row in img1_larger[y + dy: y + dy + h]]
                res = self.count_overlap(windowed_img1, img2)
                best_res = max(best_res, res)
        return best_res
    
    def count_overlap(self, img1, img2):
        res = 0
        for i in range(len(img1)):
            for j in range(len(img1)):
                res += img1[i][j] * img2[i][j]
        return res