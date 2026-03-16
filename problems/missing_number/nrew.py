import sys

def solve():
    data = sys.stdin.buffer.read().split()
     MOD = 998244353
      n, m = int(data[0]), int(data[1])
      a = list(map(int, data[2:2+n]))
      ks = list(map(int, data[2+n:2+n+m]))

     left = [-1] * n
     right = [n] * n
     stack = []
     for i in range(n):
         while stack and a[stack[-1]] >= a[i]:
             stack.pop()
         if stack: left[i] = stack[-1]
         stack.append(i)
     stack = []
     for i in range(n-1, -1, -1):
         while stack and a[stack[-1]] > a[i]:
             stack.pop()
         if stack: right[i] = stack[-1]
         stack.append(i)

     cnt = [(i - left[i]) * (right[i] - i) % MOD for i in range(n)]

     prefix = [1] * (n + 1)
     for i in range(n):
         prefix[i+1] = prefix[i] * a[i] % MOD
     inv = pow(prefix[n], MOD - 2, MOD)
     inv_a = [0] * n
     for i in range(n-1, -1, -1):
         inv_a[i] = inv * prefix[i] % MOD
         inv = inv * a[i] % MOD

     SumS = T = 0
     for i in range(n):
         SumS = (SumS + (i+1) * (n-i) % MOD * inv_a[i]) % MOD
         T    = (T    + cnt[i] * inv_a[i]) % MOD

     a_mod = [x % MOD for x in a]
     order = sorted(range(n), key=lambda i: a[i])

     N_cur = V_cur = W_cur = ptr = 0
     out = []
     for k in ks:
         thr = k + 1
         while ptr < n and a[order[ptr]] <= thr:
             i = order[ptr]
             c = cnt[i]
             N_cur = (N_cur + c) % MOD
             V_cur = (V_cur + a_mod[i] * c) % MOD
             W_cur = (W_cur + inv_a[i] * c) % MOD
             ptr += 1
         k_mod = k % MOD
         ans = (SumS + (k_mod+2)*N_cur - V_cur
                     - (k_mod+1)*W_cur + k_mod*T) % MOD
         out.append(ans)

     sys.stdout.write('\n'.join(map(str, out)))

solve()