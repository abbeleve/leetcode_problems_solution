class Solution:
    def stringCount(self, n: int) -> int:
        all_variants = 26**n
        no_l = 25**n
        no_e_or_1_e = 25**n + n*(25**(n-1))
        no_t = 25**n
        no_l_no_e_or_1_e = 24**n + n*(24**(n-1)) 
        no_l_no_t = 24**n
        no_t_no_e_or_1_e = 24**n + n*(24**(n-1))
        no_l_no_t_no_e_or_1_e = 23**n + n*(23**(n-1))
        return (all_variants - (no_l + no_e_or_1_e + no_t - no_l_no_e_or_1_e - no_l_no_t - no_t_no_e_or_1_e + no_l_no_t_no_e_or_1_e)) % (10**9 + 7)