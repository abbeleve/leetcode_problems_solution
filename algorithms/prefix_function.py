def prefix_function(s: str) -> list:
    n = len(s)
    pi = [0] * n
    k = 0
    for i in range(1, n):
        k = pi[i - 1]
        while k > 0 and s[i] != s[k]:
            k = pi[k - 1]
        if s[i] == s[k]:
            k += 1
        pi[i] = k
    return pi

print(prefix_function("aba#abcaba"))