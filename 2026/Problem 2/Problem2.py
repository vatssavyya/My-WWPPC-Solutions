t = int(input())

for i in range(t):
    var1, var2 = map(int, input().split())

    if (var1 <= 0 <= var2):
        var3 = 0
    else:
        var3 = min(abs(var1), abs(var2))

    var4 = max(abs(var1), abs(var2))

    print(var3, var4)