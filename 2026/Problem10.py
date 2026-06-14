t = int(input())

for i in range(t):
    s = input().strip()
    ans = 0
    max_digit = 0
    for c in s:
        d = int(c)
        if d < max_digit:
            ans += max_digit - d
        else:
            max_digit = d
    print(ans)