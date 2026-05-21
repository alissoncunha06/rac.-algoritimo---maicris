def generate_pa(a1, r, n):
    pa = []
    for i in range(n - 1):
        pa.append(pa[i] + r)
    return pa

