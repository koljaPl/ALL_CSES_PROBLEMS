import sys
import numpy as np

def solve():
    data = sys.stdin.read().split()
    n, m, mod = int(data[0]), int(data[1]), int(data[2])

    if n == 1:
        print(m % mod)
        return

    size = 2 * m
    I_mat = np.eye(size, dtype=np.int64)

    T = np.zeros((size, size), dtype=np.int64)
    for i in range(m):
        for j in range(i):
            T[i, j] = (-(i - j)) % mod  # F'-F: -(l'-l)
            T[i, m + j] = (-(j + 1)) % mod  # F'-G: -r
    for i in range(m):
        for j in range(i + 1):
            T[m + i, j] = (m - j) % mod  # G'-F: (m-l+1)
    for i in range(m):
        for j in range(m):
            T[m + i, m + j] = (min(i, j) + 1) % mod  # G'-G: min(r,r')

    def matmul(A, B):
        C = np.zeros((size, size), dtype=np.int64)
        for s in range(0, size, 8):
            e = min(s + 8, size)
            C += A[:, s:e] @ B[s:e, :]
            C %= mod
        return C

    def matvec(M, v):
        r = np.zeros(size, dtype=np.int64)
        for s in range(0, size, 8):
            e = min(s + 8, size)
            r += M[:, s:e] @ v[s:e]
            r %= mod
        return r

    def power_and_sum(k):
        """Возвращает (T^k, I + T + ... + T^{k-1})"""
        if k == 1:
            return T.copy(), I_mat.copy()
        if k % 2 == 0:
            Th, Sh = power_and_sum(k // 2)
            T2 = matmul(Th, Th)
            S2 = matmul((I_mat + Th) % mod, Sh)
            return T2, S2
        else:
            Tm1, Sm1 = power_and_sum(k - 1)
            Tk = matmul(Tm1, T)
            Sk = (Sm1 + Tm1) % mod
            return Tk, Sk

    _, S = power_and_sum(n - 1)

    # Начальный вектор v₂: F₂[l] = m-l+1, G₂[r] = 0
    v2 = np.zeros(size, dtype=np.int64)
    for l in range(1, m + 1):
        v2[l - 1] = (m - l + 1) % mod

    Sv = matvec(S, v2)

    # Вектор весов: w[l-1] = m-l+1, w[m+r-1] = r
    w = np.zeros(size, dtype=np.int64)
    for l in range(1, m + 1):
        w[l - 1] = m - l + 1
    for r in range(1, m + 1):
        w[m + r - 1] = r

    ans = (m % mod + int(np.dot(w, Sv)) % mod) % mod
    print(ans)


solve()

