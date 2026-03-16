import sys
import numpy as np

def solve():
    n, m, mod = map(int, sys.stdin.read().split())

    if n == 1:
        print(m % mod)
        return

    sz = 2 * m
    CHUNK = 8  # безопасный размер блока, чтобы не переполнить int64

    def mmul(A, B):
        C = np.zeros((sz, sz), dtype=np.int64)
        for i in range(0, sz, CHUNK):
            C += A[:, i:i+CHUNK] @ B[i:i+CHUNK]
            C %= mod
        return C

    # Строим матрицу перехода T (2m × 2m)
    a = np.arange(m)
    ii, jj = np.meshgrid(a, a, indexing='ij')  # ii[i,j]=i, jj[i,j]=j
    lo, le = jj < ii, jj <= ii                 # нижний треугольник

    T = np.zeros((sz, sz), dtype=np.int64)
    T[:m, :m][lo] = (jj - ii)[lo] % mod    # F'←F: -(i-j)
    T[:m, m:][lo] = (-jj - 1)[lo] % mod    # F'←G: -(j+1)
    T[m:, :m][le] = (m - jj)[le]           # G'←F: m-j
    T[m:, m:]     = np.minimum(ii, jj) + 1  # G'←G: min(i,j)+1
    T %= mod

    I = np.eye(sz, dtype=np.int64)

    def pow_sum(k):
        """Возвращает (T^k, I + T + ... + T^{k-1})"""
        if k == 1:
            return T.copy(), I.copy()
        if k % 2 == 0:
            Th, Sh = pow_sum(k // 2)
            return mmul(Th, Th), mmul((I + Th) % mod, Sh)
        Tm1, Sm1 = pow_sum(k - 1)
        return mmul(Tm1, T), (Sm1 + Tm1) % mod

    _, S = pow_sum(n - 1)

    # Начальный вектор строки 2: f[l-1] = m-l+1
    v = np.zeros(sz, dtype=np.int64)
    v[:m] = m - a

    Sv = np.zeros(sz, dtype=np.int64)
    for i in range(0, sz, CHUNK):
        Sv += S[:, i:i+CHUNK] @ v[i:i+CHUNK]
        Sv %= mod

    # Вектор весов w: суммируем по всем [l,r]
    w = np.concatenate([m - a, a + 1])  # w[l-1]=m-l+1, w[m+r-1]=r
    print((m + int(w @ Sv % mod)) % mod)

solve()