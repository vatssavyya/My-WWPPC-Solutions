t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    sum1 = 0
    total1 = 0
    for j in range(n-1, -1, -1):
        sum1 += a[j]
        total1 += (sum1 + k - 1) // k

    print(2 * total1)