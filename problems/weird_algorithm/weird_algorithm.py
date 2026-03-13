n = int(input())
ans = []
ans.append(n)

while n != 1:
    if n % 2 == 0:
        n /= 2
        ans.append(int(n))
    else:
        n = n * 3 + 1
        ans.append(int(n))

print(*ans)