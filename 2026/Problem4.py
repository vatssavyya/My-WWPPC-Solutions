t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if (n % 2) == 1:
        print("YES")
    else:
        if (sum(a) % 2 == 0):
            print("YES")
        else:
            print("NO")