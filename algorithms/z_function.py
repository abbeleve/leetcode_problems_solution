def z_function(s: str) -> list:
    n = len(s)
    z = [0]
    for i in range(1, n):
        k = z[i - 1]
        if z[k] != z[i]:
            
        if z[k] == z[i]:
            k += 1
        z[i] = k
