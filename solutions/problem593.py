class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False
        if p1 == p2 or p2 == p3 or p3 == p4 or p1 == p4 or p1 == p3 or p2 == p4:
            return False
            
        if self.checkIfVectorsAreDiagonals(p1, p2, p3, p4):
            pass
        elif self.checkIfVectorsAreDiagonals(p1, p3, p2, p4):
            p2, p3 = p3, p2
        elif self.checkIfVectorsAreDiagonals(p1, p4, p2, p3):
            p2, p3, p4 = p4, p2, p3
        else:
            return False
        diag_1 = [p2[0] - p1[0], p2[1] - p1[1]]
        diag_2 = [p4[0] - p3[0], p4[1] - p3[1]]
        dot_product = diag_1[0] * diag_2[0] + diag_1[1] * diag_2[1]
        if dot_product != 0:
            return False
        len_d1_sq = diag_1[0]**2 + diag_1[1]**2
        len_d2_sq = diag_2[0]**2 + diag_2[1]**2
        if len_d1_sq != len_d2_sq:
            return False
        M1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        M2 = ((p3[0] + p4[0]) / 2, (p3[1] + p4[1]) / 2)
        if M1 != M2:
            return False
        return True

    def checkIfVectorsAreDiagonals(self, p1, p2, p3, p4):
        vector_normal = [-(p2[1] - p1[1]), p2[0] - p1[0]]
        v3 = [p3[0] - p1[0], p3[1] - p1[1]]
        v4 = [p4[0] - p1[0], p4[1] - p1[1]]
        scalar_p3 = vector_normal[0] * v3[0] + vector_normal[1] * v3[1]
        scalar_p4 = vector_normal[0] * v4[0] + vector_normal[1] * v4[1]
        if scalar_p3 * scalar_p4 < 0:
            return True
        return False