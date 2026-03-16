import sys
input = sys.stdin.readline

MOD = 998244353

n, m = map(int, input().split())
list_a = list(map(int, input().split()))
quer = list(map(int, input().split()))

prev_smaller = [-1] * n
next_smaller  = [n] * n

stack = []
for i in range(n):
    while stack and list_a[stack[-1]] >= list_a[i]:
        stack.pop()
    if stack:
        prev_smaller[i] = stack[-1]
    stack.append(i)

stack = []
for i in range(n - 1, -1, -1):
    while stack and list_a[stack[-1]] > list_a[i]:
        stack.pop()
    if stack:
        next_smaller[i] = stack[-1]
    stack.append(i)

subarray_count = [(i - prev_smaller[i]) * (next_smaller[i] - i) % MOD for i in range(n)]

prefix_product = [1] * (n + 1)
for i in range(n):
    prefix_product[i + 1] = prefix_product[i] * list_a[i] % MOD

inv_total = pow(prefix_product[n], MOD - 2, MOD)
inv_array = [0] * n
for i in range(n - 1, -1, -1):
    inv_array[i] = inv_total * prefix_product[i] % MOD
    inv_total = inv_total * list_a[i] % MOD

sum_all_inv = sum_min_inv = 0
for i in range(n):
    sum_all_inv = (sum_all_inv + (i + 1) * (n - i) % MOD * inv_array[i]) % MOD
    sum_min_inv = (sum_min_inv + subarray_count[i] * inv_array[i]) % MOD

array_mod  = [x % MOD for x in list_a]
sorted_idx = sorted(range(n), key=lambda i: list_a[i])

count_small = 0
val_small   = 0
inv_small   = 0
ptr = 0

for k in quer:
    threshold = k + 1
    while ptr < n and list_a[sorted_idx[ptr]] <= threshold:
        idx = sorted_idx[ptr]
        cnt = subarray_count[idx]
        count_small = (count_small + cnt) % MOD
        val_small   = (val_small   + array_mod[idx] * cnt) % MOD
        inv_small   = (inv_small   + inv_array[idx] * cnt) % MOD
        ptr += 1

    k_mod = k % MOD
    ans = (sum_all_inv + (k_mod + 2) * count_small - val_small
                       - (k_mod + 1) * inv_small   + k_mod * sum_min_inv) % MOD
    print(ans)